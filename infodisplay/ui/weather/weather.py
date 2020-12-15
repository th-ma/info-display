# -*- coding: utf-8 -*-
import json

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from loguru import logger
import paho.mqtt.client as mqttClient

from infodisplay.utils.file_utils import dump_dict2json_file, save_jsondata_2_jsonfile

CLIENT_ID = 'DELETE_999'
PORT = 1883
HOST = 'rp3'


class WeatherDataThread(QThread):
    signal_msg = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.client = mqttClient.Client(CLIENT_ID)

    def on_connect_cb(self, client, userdata, flags, rc):
        logger.info(f'connected to broker with result code: {str(rc)}')
        self.client.subscribe('infoscreens/weather/#')
        self.connected = True

    def on_message_cb(self, client, userdata, msg):
        logger.info(f'message received -> topic: {msg.topic}, payload: {str(msg.payload)}')
        payload = (msg.payload.decode('utf-8'))
        self.signal_msg.emit(msg.topic, str(payload))

    def run(self):
        logger.info(f'WeatherDataThread')
        self.client.on_connect = self.on_connect_cb
        self.client.on_message = self.on_message_cb
        self.client.connect(HOST, PORT)
        self.client.loop_forever()


class Weather(QWidget):
    def __init__(self, parent=None):
        super(Weather, self).__init__(parent)
        if parent:
            self.setFixedSize(parent.width(), parent.height())

        self.thread = WeatherDataThread()
        self.start_threads()

        # self.refresh_timer = QTimer()

        logger.info(f'with: {parent.width()}, height: {parent.height()}')
        self.testUI()

    def start_threads(self):
        self.thread.signal_msg.connect(self.message_received_cb)
        self.thread.start()

    def message_received_cb(self, topic, payload):
        logger.info(f'message_received_cb t: {topic}, p:{payload}')
        if topic == 'infoscreens/weather/current':
            filenanme = 'infodisplay/ui/weather/res/current_weather.json'
        elif topic == 'infoscreens/weather/forecast':
            filenanme = 'infodisplay/ui/weather/res/weather_forecast.json'
        else:
            logger.error(f'unknown topic: {topic}')
            return
        d = json.loads(payload)
        logger.info(f'd, type: {type(d)}')
        save_jsondata_2_jsonfile(filenanme, d)


    def testUI(self):
        test = QLabel("Laber", self)
        test.move(100, 0)
        test.setText("alalalal\nkaksksk\tndndnd")
        self.show()
