# -*- coding: utf-8 -*-
import json
import threading

import time
from loguru import logger

from configs.config_weather import ConfigWeather, ConfigWeatherServer
from infodisplay.server.weatherServer.weather_provider import AccuWeather
from infodisplay.utils.file_utils import get_dict_from_json_file, mqtt_send_json_file
from infodisplay.utils.mqtt_client import MqttClient

INTERVAL = 60 * 60  # time in seconds -> 1h


class WeatherServer(threading.Thread):

    def __init__(self, thread_id, run_event):
        threading.Thread.__init__(self)

        self.threadID = thread_id
        self.run_event = run_event
        self.mqtt_client = MqttClient(ConfigWeather.MQTT_HOST,
                                      ConfigWeather.MQTT_BASE_TOPIC,
                                      ConfigWeather.MQTT_TOPIC)

    def run(self):
        while self.run_event.is_set():
            try:
                logger.info(f'Weather thread (re)started')
                # device = IDevicePeripheral(self.mac_address, "iGrillv2")
                accu_weather = AccuWeather()
                while True:
                    accu_weather.update_weather_data()
                    logger.info(f'--> accu_weather.update_weather_data()')
                    # push mqtt
                    current = mqtt_send_json_file(ConfigWeatherServer.JSON_CURRENT_WEATHER)
                    self.mqtt_client.publish("current", current)

                    forecast = mqtt_send_json_file(ConfigWeatherServer.JSON_WEATHER_FORECAST)
                    self.mqtt_client.publish("forecast", forecast)
                    time.sleep(INTERVAL)
            except Exception as e:
                logger.error(f'error occured: {e}')
                logger.error(f'sleeping for {INTERVAL} seconds before retrying')
                time.sleep(INTERVAL)
        logger.info(f'"Thread exiting')
