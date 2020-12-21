# -*- coding: utf-8 -*-
import json

import requests
from loguru import logger

from configs.config_weather import ConfigWeatherServer
from infodisplay.server.weatherServer.weather_objects import WeatherForecast, CurrentWeather
from infodisplay.utils.file_utils import file_get_last_modification_date, get_dict_from_json_file, dump_dict2json_file, \
    save_jsondata_2_jsonfile, does_file_exist
from infodisplay.utils.timedate_utils import get_time_diff_from_date_string, get_now_as_string


class AccuWeather:
    """ Weather provider Accu Weather """

    def __init__(self):
        self.weather_forecast = WeatherForecast(ConfigWeatherServer.JSON_WEATHER_FORECAST,
                                                ConfigWeatherServer.UPDATE_INTERVAL_FORECAST)
        self.current_weather = CurrentWeather(ConfigWeatherServer.JSON_CURRENT_WEATHER,
                                              ConfigWeatherServer.UPDATE_INTERVAL_CURRENT)
        self.status_file = ConfigWeatherServer.JSON_STATUS
        self.last_connection = None
        self.connections_left = -1

    def update_weather_data(self):
        logger.info(f'--> update_weather_data()')
        if not self._check_status_header():
            logger.error(f'status header check failed')
            return
        self._update_forecast()
        self._update_current_weather()

    def update_forecast(self):
        logger.info(f'--> update_forecast()')
        if not self._check_status_header():
            logger.error(f'status header check failed')
            return
        self._update_forecast()

    def update_current_weather(self):
        logger.info(f'--> update_current_weather()')
        if not self._check_status_header():
            logger.error(f'status header check failed')
            return
        self._update_current_weather()

    def _update_forecast(self):
        logger.debug(f'--> _update_forecast')
        diff = get_time_diff_from_date_string(self.weather_forecast.last_update)
        logger.debug(f'diff: {diff}, update cycle: {self.weather_forecast.update_cycle}')
        diff  = 5
        if int(diff) > self.weather_forecast.update_cycle:
            logger.info(f'_update_forecast after {int(diff)} hours')
            logger.info(f'call _fetch_data_from_url ({self.weather_forecast.json_file})')
            self.connections_left = self._fetch_data_from_url(ConfigWeatherServer.URL_FORECAST,
                                                              self.weather_forecast.json_file)
            self._update_last_connection_counter()
            self.weather_forecast.last_update = file_get_last_modification_date(self.weather_forecast.json_file)

    def _update_current_weather(self):
        logger.debug(f'--> _update_current_weather')
        diff = get_time_diff_from_date_string(self.current_weather.last_update)
        logger.debug(f'diff: {diff}, update cycle: {self.current_weather.update_cycle}')
        diff = 5
        if int(diff) > self.current_weather.update_cycle:
            logger.info(f'_update_current_weather after {int(diff)} hours')
            logger.info(f'call _fetch_data_from_url ({self.current_weather.json_file})')
            self.connections_left = self._fetch_data_from_url(ConfigWeatherServer.URL_CURRENT,
                                                              self.current_weather.json_file)
            self._update_last_connection_counter()
            self.current_weather.last_update = file_get_last_modification_date(self.current_weather.json_file)

    def _fetch_data_from_url(self, url, filename):
        try:
            response = requests.get(url)
            response.raise_for_status()
            rate_remaining = response.headers._store['ratelimit-remaining'][1]
            data = json.loads(response.text)
            self._save_data_to_file(filename, data)
            return rate_remaining
        except requests.exceptions.HTTPError as e:
            logger.error(f'Fetch error: {e.response.text}')

    def _update_last_connection_counter(self):
        tmp = get_dict_from_json_file(self.status_file)
        tmp['header']['connections_left'] = self.connections_left
        tmp['header']['last_connection'] = get_now_as_string()
        dump_dict2json_file(self.status_file, tmp)

    def _save_data_to_file(self, filename, data):
        save_jsondata_2_jsonfile(filename, data)

    def _check_status_header(self):
        header = get_dict_from_json_file(self.status_file)
        last_connection = header['header']['last_connection']
        connections_left = header['header']['connections_left']

        if connections_left == 0:
            logger.info(f'No more connections possible due too Accu Weather limitations for free accounts')
            if last_connection is not None:
                diff_hours = get_time_diff_from_date_string(last_connection)
                if diff_hours > 24.0:  # reset after one day
                    self.connections_left = 50
                    return True
                else:
                    return False
            else:
                return True
        else:
            return True

    def _update_status_file(self):
        tmp = get_dict_from_json_file(self.status_file)
        tmp = self._update_status_dict(tmp)
        dump_dict2json_file(self.status_file, tmp)

    def _update_status_dict(self, dic: dict):
        dic['header']['last_connection'] = self.last_connection
        dic['header']['connections_left'] = self.connections_left
        dic['current_weather']['last_update'] = self.current_weather.last_update
        dic['current_weather']['update_needed'] = self.current_weather.update_needed
        dic['weather_forecast']['last_update'] = self.weather_forecast.last_update
        dic['weather_forecast']['update_needed'] = self.weather_forecast.update_needed
        return dic

    def _initStatusFile(self):
        if not does_file_exist(self.status_file):
            # create new file with default dict
            dic = ConfigWeatherServer.STATUS_DICT
            dic = self._update_status_dict(dic)
            dump_dict2json_file(self.status_file, dic)
