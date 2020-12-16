# -*- coding: utf-8 -*-
import json
import threading

import time
from loguru import logger

from configs.config_weather import ConfigWeather, ConfigWeatherServer
from infodisplay.server.weatherServer.weather_provider import AccuWeather
from infodisplay.utils.file_utils import get_dict_from_json_file, mqtt_send_json_file
from infodisplay.utils.mqtt_client import MqttClient


class WeatherServer(threading.Thread):

    def __init__(self, thread_id, run_event):
        threading.Thread.__init__(self)

        self.threadID = thread_id
        self.run_event = run_event
        self.mqtt_client = MqttClient(ConfigWeather.MQTT_HOST,
                                      ConfigWeather.MQTT_BASE_TOPIC,
                                      ConfigWeather.MQTT_TOPIC)
        self.update_interval = ConfigWeatherServer.UPDATE_INTERVAL_CURRENT
        self.forecast_counter = ConfigWeatherServer.UPDATE_INTERVAL_FORECAST

    def run(self):
        while self.run_event.is_set():
            try:
                logger.info(f'Weather thread (re)started')
                # device = IDevicePeripheral(self.mac_address, "iGrillv2")
                accu_weather = AccuWeather()
                while True:
                    logger.info(f'self.forecast_counter: {self.forecast_counter}')
                    accu_weather.update_current_weather()
                    accu_weather.update_weather_data()
                    logger.info(f'--> accu_weather.update_current_weather()')
                    current = mqtt_send_json_file(ConfigWeatherServer.JSON_CURRENT_WEATHER)
                    self.mqtt_client.publish("current", current)

                    if self.forecast_counter == ConfigWeatherServer.UPDATE_INTERVAL_FORECAST:
                        self.forecast_counter = 0
                        forecast = mqtt_send_json_file(ConfigWeatherServer.JSON_WEATHER_FORECAST)
                        self.mqtt_client.publish("forecast", forecast)
                        logger.info(f'--> accu_weather.update_weather_forecast()')

                    self.forecast_counter += 1
                    time.sleep(self.update_interval)
            except Exception as e:
                logger.error(f'error occured: {e}')
                logger.error(f'sleeping for {self.update_interval} seconds before retrying')
                time.sleep(self.update_interval)
        logger.info(f'"Thread exiting')
