# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLabel
from loguru import logger

from configs.config_weather import ConfigWeather
from infodisplay.ui.weather.weather_thread import WeatherDataThread


class Weather(QWidget):
    def __init__(self, parent=None):
        super(Weather, self).__init__(parent)
        if parent:
            self.setFixedSize(parent.width(), parent.height())

        self.thread = WeatherDataThread()
        self.start_threads()

        self._update_current_weather()
        self._update_weather_forecast()

        logger.info(f'with: {parent.width()}, height: {parent.height()}')
        self.testUI()

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
        filename = ConfigWeather.JSON_CURRENT_WEATHER
        logger.info(f'_update_current_weather')

    def _update_weather_forecast(self):
        filename = ConfigWeather.JSON_WEATHER_FORECAST
        logger.info(f'_update_weather_forecast')

    def testUI(self):
        test = QLabel("Laber", self)
        test.move(0, 0)
        test.setText("alalalal\nkaksksk\tndndnd")
        self.show()
