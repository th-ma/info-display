# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from loguru import logger

from configs.config_weather import ConfigWeather, lblHeader, lblText
from infodisplay.ui.weather.weather_forecast import WeatherForecast
from infodisplay.ui.weather.weather_indoor import WeatherIndoor
from infodisplay.ui.weather.weather_outdoor import WeatherOutdooor

from infodisplay.ui.weather.weather_thread import WeatherDataThread
from infodisplay.ui.weather.weather_time_date import WeatherTimeDate
from infodisplay.utils.file_utils import get_dict_from_json_file


class Weather(QWidget):
    def __init__(self, parent=None):
        super(Weather, self).__init__(parent)
        if parent:
            self.setFixedSize(parent.width(), parent.height())

        self.thread = WeatherDataThread()
        self.start_threads()

        logger.info(f'with: {parent.width()}, height: {parent.height()}')
        # read data
        self.forecast = get_dict_from_json_file(ConfigWeather.JSON_WEATHER_FORECAST)
        self.current = get_dict_from_json_file(ConfigWeather.JSON_CURRENT_WEATHER)
        # define regions
        self.region_outdoor = self.createRegionOutdoor()
        self.region_time_date = self.createRegionTimeAndDate()
        self.region_forecast = self.createRegionForecast()
        self.region_indoor = self.createRegionIndoor()
        # update UI
        self.outdoor_ui = WeatherOutdooor(self.region_outdoor)
        self.forecast_ui = WeatherForecast(self.region_forecast)
        self.time_date_ui = WeatherTimeDate(self.region_time_date)
        self.indoor_ui = WeatherIndoor(self.region_indoor)

        self._update_current_weather()
        self._update_weather_forecast()

        logger.info(f'w: {self.region_time_date.width()}, h: {self.region_time_date.height()}')

    def _get_center_x(self, text, w):
        fm = QFontMetrics(text.font())
        font_width = fm.width(text.text())
        x = w - font_width
        return x / 2

    def start_threads(self):
        self.thread.signal_msg.connect(self.message_received_cb)
        self.thread.start()

    def message_received_cb(self, topic):
        logger.info(f'message_received_cb t: {topic}')
        if topic == ConfigWeather.MQTT_TOPIC_CURRENT:
            self._update_current_weather()
        elif topic == ConfigWeather.MQTT_TOPIC_FORECAST:
            self._update_weather_forecast()
        else:
            logger.error(f'unknown topic: {topic}')
            return

    def _update_current_weather(self):
        logger.info(f'_update_current_weather')
        self.current = get_dict_from_json_file(ConfigWeather.JSON_CURRENT_WEATHER)
        self.outdoor_ui.updateData(self.current)

    def _update_weather_forecast(self):
        logger.info(f'_update_weather_forecast')
        self.forecast = get_dict_from_json_file(ConfigWeather.JSON_WEATHER_FORECAST)

    def createRegionOutdoor(self) -> QFrame:
        region_outdoor = QFrame(self)
        region_outdoor.setObjectName(ConfigWeather.REGION_OUTDOOR_NAME)

        region_outdoor.setStyleSheet(ConfigWeather.REGION_OUTDOOR_STYLESHEET)
        region_outdoor.setGeometry(ConfigWeather.REGION_OUTDOOR_X,
                                   ConfigWeather.REGION_OUTDOOR_Y,
                                   ConfigWeather.REGION_OUTDOOR_WIDTH,
                                   ConfigWeather.REGION_OUTDOOR_HEIGHT)
        return region_outdoor

    def createRegionTimeAndDate(self) -> QFrame:
        region_time_date = QFrame(self)
        region_time_date.setObjectName(ConfigWeather.REGION_TIME_DATE_NAME)
        region_time_date.setStyleSheet(ConfigWeather.REGION_TIME_DATE_STYLESHEET)
        region_time_date.setGeometry(ConfigWeather.REGION_TIME_DATE_X,
                                     ConfigWeather.REGION_TIME_DATE_Y,
                                     ConfigWeather.REGION_TIME_DATE_WIDTH,
                                     ConfigWeather.REGION_TIME_DATE_HEIGHT)
        return region_time_date

    def createRegionForecast(self) -> QFrame:
        region_forecast = QFrame(self)
        region_forecast.setObjectName(ConfigWeather.REGION_FORECAST_NAME)

        region_forecast.setStyleSheet(ConfigWeather.REGION_FORECAST_STYLESHEET)
        region_forecast.setGeometry(ConfigWeather.REGION_FORECAST_X,
                                    ConfigWeather.REGION_FORECAST_Y,
                                    ConfigWeather.REGION_FORECAST_WIDTH,
                                    ConfigWeather.REGION_FORECAST_HEIGHT)
        return region_forecast

    def createRegionIndoor(self) -> QFrame:
        region_indoor = QFrame(self)
        region_indoor.setObjectName(ConfigWeather.REGION_INDOOR_NAME)
        region_indoor.setStyleSheet(ConfigWeather.REGION_INDOOR_STYLESHEET)
        region_indoor.setGeometry(ConfigWeather.REGION_INDOOR_X,
                                  ConfigWeather.REGION_INDOOR_Y,
                                  ConfigWeather.REGION_INDOOR_WIDTH,
                                  ConfigWeather.REGION_INDOOR_HEIGHT)
        return region_indoor
