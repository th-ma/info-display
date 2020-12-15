# -*- coding: utf-8 -*-
import hashlib
import json

import paho.mqtt.client as mqtt
from loguru import logger

from infodisplay.utils.file_utils import get_dict_from_json_file


class MqttClient:
    def __init__(self, host, base_topic, topic):
        self.host = host
        self.base_topic = base_topic
        self.topic = topic

        self.client = mqtt.Client()
        self._connect_client()

    def _connect_client(self):
        ret = self.client.connect(self.host)
        logger.info(f'connect returns: {ret}')

    def publish(self, topic: str, value: str):
        logger.info(f'{self.base_topic}/{self.topic}/{topic} -> {value}')
        self.client.publish(f'{self.base_topic}/{self.topic}/{topic}', value)
        #self.test_mqtt()


    def test_mqtt(self):
        out_hash_md5 = hashlib.md5()
        filename = 'infodisplay/server/weatherServer/res/accu_current_weather.json'
        end = "end" + ",," + filename + ",," + out_hash_md5.hexdigest()
        send = get_dict_from_json_file(filename)
        logger.info(send)
        logger.info(str(send))
        data = json.dumps(send)
        self.client.publish(f'{self.base_topic}/{self.topic}', data)
