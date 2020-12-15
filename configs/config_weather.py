# -*- coding: utf-8 -*-
from dataclasses import dataclass


##########################################################################
# Weather GUI
##########################################################################
@dataclass
class ConfigWeather:
    REFRESH_TIME: int = 1000 * 60 * 1

    MQTT_HOST: str = 'rp3'
    MQTT_BASE_TOPIC: str = 'infoscreens'
    MQTT_TOPIC: str = 'weather'

##########################################################################
# Weather Server
##########################################################################
@dataclass
class ConfigWeatherServer:
    JSON_CURRENT_WEATHER: str   = 'infodisplay/server/weatherServer/res/accu_current_weather.json'
    JSON_WEATHER_FORECAST: str = 'infodisplay/server/weatherServer/res/accu_forecast_weather.json'
    JSON_STATUS: str = 'infodisplay/server/weatherServer/res/accu_status.json'
    API_KEY: str = 'GRwYjHLdIa4q1ryLomhvqNJiKTjfntbs'
    URL_CURRENT: str = 'http://dataservice.accuweather.com/currentconditions/v1/176968?apikey=GRwYjHLdIa4q1ryLomhvqNJiKTjfntbs&language=de-De&details=true'
    URL_FORECAST: str = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/176968?apikey=GRwYjHLdIa4q1ryLomhvqNJiKTjfntbs&language=de-De&details=true&metric=true'
    UPDATE_INTERVAL_FORECAST: int = 4
    UPDATE_INTERVAL_CURRENT: int = 1
    ###
    # Default dict in case no status file is available
    ###
    STATUS_DICT = {
        "header":
            {
                "last_connection": None,
                "connections_left": -1
            },
        "current_weather":
            {
                "last_update": "none",
                "update_needed": False
            },
        "weather_forecast":
            {
                "last_update": "none",
                "update_needed": False
            }
    }

