# -*- coding: utf-8 -*-
import json

from PyQt5.QtCore import QThread, pyqtSignal
import paho.mqtt.client as mqttClient
from loguru import logger

from configs.config_weather import ConfigWeather
from infodisplay.utils.file_utils import save_jsondata_2_jsonfile


class WeatherDataThread(QThread):
    signal_msg = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.client = mqttClient.Client(ConfigWeather.MQTT_CLIENT_ID)

    def on_connect_cb(self, client, userdata, flags, rc):
        logger.info(f'connected to broker with result code: {str(rc)}')
        self.client.subscribe('infoscreens/weather/#', qos=2)
        self.connected = True

    def on_message_cb(self, client, userdata, msg):
        # logger.info(f'message received -> topic: {msg.topic}, payload: {str(msg.payload)}')
        logger.info(f'message received -> topic: {msg.topic}')
        payload = (msg.payload.decode('utf-8'))
        self._save_received_data_to_file(msg.topic, payload)
        self.signal_msg.emit(msg.topic)

    def _save_received_data_to_file(self, topic, payload):
        if topic == ConfigWeather.MQTT_TOPIC_CURRENT:
            filename = ConfigWeather.JSON_CURRENT_WEATHER
        elif topic == ConfigWeather.MQTT_TOPIC_FORECAST:
            filename = ConfigWeather.JSON_WEATHER_FORECAST
        else:
            logger.error(f'unknown topic: {topic}')
            return
        logger.debug(f'_save_received_data_to_file -> file: {filename}')
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
