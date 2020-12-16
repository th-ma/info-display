# -*- coding: utf-8 -*-
from dataclasses import dataclass


##########################################################################
# Weather GUI
##########################################################################
@dataclass
class ConfigWeather:
    REFRESH_TIME: int           = 1000 * 60 * 1  # TODO: check if used
    # MQTT Configuration
    MQTT_PORT: int              = 1883   # default port
    MQTT_HOST: str              = 'rp3'  # host name of the broker
    MQTT_BASE_TOPIC: str        = 'infoscreens'
    MQTT_TOPIC: str             = 'weather'
    MQTT_CLIENT_ID: str         = 'DELETE_999'
    MQTT_TOPIC_CURRENT: str     = 'infoscreens/weather/current'
    MQTT_TOPIC_FORECAST: str    = 'infoscreens/weather/forecast'
    # JSON files used by the UI Application
    JSON_CURRENT_WEATHER: str = 'infodisplay/ui/weather/res/current_weather.json'
    JSON_WEATHER_FORECAST: str = 'infodisplay/ui/weather/res/weather_forecast.json'


##########################################################################
# Weather Server
##########################################################################
@dataclass
class ConfigWeatherServer:
    # JSON files used by weather server
    JSON_CURRENT_WEATHER: str       = 'infodisplay/server/weatherServer/res/accu_current_weather.json'
    JSON_WEATHER_FORECAST: str      = 'infodisplay/server/weatherServer/res/accu_forecast_weather.json'
    JSON_STATUS: str                = 'infodisplay/server/weatherServer/res/accu_status.json'
    # Accu Weather configuration
    API_KEY: str                    = 'GRwYjHLdIa4q1ryLomhvqNJiKTjfntbs'
    URL_CURRENT: str                = 'http://dataservice.accuweather.com/currentconditions/v1/176968?apikey=GRwYjHLdIa4q1ryLomhvqNJiKTjfntbs&language=de-De&details=true'
    URL_FORECAST: str               = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/176968?apikey=GRwYjHLdIa4q1ryLomhvqNJiKTjfntbs&language=de-De&details=true&metric=true'
    # timer for update calls to weather provider
    UPDATE_INTERVAL_CURRENT: int    = 60 * 60 * 1   # 1 hour
    UPDATE_INTERVAL_FORECAST: int   = 4             # 4 times current then forecast again

    # Default dict in case no status file is available
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
