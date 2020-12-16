# -*- coding: utf-8 -*-
import json

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from loguru import logger
import paho.mqtt.client as mqttClient

from configs.config_weather import ConfigWeather
from infodisplay.utils.file_utils import dump_dict2json_file, save_jsondata_2_jsonfile


class WeatherDataThread(QThread):
    signal_msg = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.client = mqttClient.Client(ConfigWeather.MQTT_CLIENT_ID)

    def on_connect_cb(self, client, userdata, flags, rc):
        logger.info(f'connected to broker with result code: {str(rc)}')
        self.client.subscribe('infoscreens/weather/#')
        self.connected = True

    def on_message_cb(self, client, userdata, msg):
        logger.info(f'message received -> topic: {msg.topic}, payload: {str(msg.payload)}')
        payload = (msg.payload.decode('utf-8'))
        self._save_received_data_to_file(msg.topic, msg.payload)
        self.signal_msg.emit(msg.topic)

    def _save_received_data_to_file(self, topic, payload):
        if topic == ConfigWeather.MQTT_TOPIC_CURRENT:
            filename = ConfigWeather.MQTT_TOPIC_CURRENT
        elif topic == ConfigWeather.MQTT_TOPIC_FORECAST:
            filename = ConfigWeather.JSON_WEATHER_FORECAST
        else:
            logger.error(f'unknown topic: {topic}')
            return
        d = json.loads(payload)
        logger.info(f'd, type: {type(d)}')
        save_jsondata_2_jsonfile(filename, d)

    def run(self):
        logger.info(f'WeatherDataThread started')
        self.client.on_connect = self.on_connect_cb
        self.client.on_message = self.on_message_cb
        try:
            self.client.connect(ConfigWeather.MQTT_HOST, ConfigWeather.MQTT_PORT)
            self.client.loop_forever()
        except Exception as e:
            logger.error(f'Connection to weather MQTT broker on host: {ConfigWeather.MQTT_HOST} failed with error: {e}')


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
