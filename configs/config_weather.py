# -*- coding: utf-8 -*-
from dataclasses import dataclass


##########################################################################
# Weather GUI
##########################################################################
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


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
    JSON_CURRENT_WEATHER: str   = 'infodisplay/ui/weather/res/current_weather.json'
    JSON_WEATHER_FORECAST: str  = 'infodisplay/ui/weather/res/weather_forecast.json'
    # Regions
    REGION_BORDER: int          = 10
    REGION_TOP: int             = 0
    REGION_DISTANCE: int        = 2
    # outdoor
    REGION_OUTDOOR_NAME: str    = 'region_outdoor'
    REGION_OUTDOOR_X: int       = 0 + REGION_BORDER
    REGION_OUTDOOR_Y: int       = REGION_TOP
    REGION_OUTDOOR_WIDTH: int   = 300
    REGION_OUTDOOR_HEIGHT: int  = 500 - 1
    # time date
    REGION_TIME_DATE_NAME: str  = 'region_time_date'
    REGION_TIME_DATE_X: int     = REGION_OUTDOOR_X + REGION_OUTDOOR_WIDTH + REGION_DISTANCE
    REGION_TIME_DATE_Y: int     = REGION_TOP
    REGION_TIME_DATE_WIDTH: int = 400
    REGION_TIME_DATE_HEIGHT: int= 200 - REGION_DISTANCE
    # forecast
    REGION_FORECAST_NAME: str   = 'region_forecast'
    REGION_FORECAST_X: int      = REGION_TIME_DATE_X # below time / date, same size
    REGION_FORECAST_Y: int      = REGION_TIME_DATE_Y + REGION_TIME_DATE_HEIGHT + REGION_DISTANCE+ REGION_DISTANCE
    REGION_FORECAST_WIDTH: int  = REGION_TIME_DATE_WIDTH
    REGION_FORECAST_HEIGHT: int = 300 - REGION_DISTANCE
    # indoor
    REGION_INDOOR_NAME: str     = 'region_indoor'
    REGION_INDOOR_X: int        = REGION_FORECAST_X + REGION_FORECAST_WIDTH + REGION_DISTANCE
    REGION_INDOOR_Y: int        = REGION_TOP
    REGION_INDOOR_WIDTH: int    = REGION_OUTDOOR_WIDTH
    REGION_INDOOR_HEIGHT: int   = REGION_OUTDOOR_HEIGHT

    # style sheets
    BACK: str = "infodisplay/ui/weather/res/outdoor_day.jpeg"
    BORDER_RADIUS: str          = '10px'
    REGION_OUTDOOR_STYLESHEET   = f"#{REGION_OUTDOOR_NAME}{{" \
                                f"border: 1px solid black; " \
                                f"background-image: url('{BACK}');" \
                                f"border-radius: {BORDER_RADIUS};}}"

    REGION_TIME_DATE_STYLESHEET = f"#{REGION_TIME_DATE_NAME}{{" \
                                f"border: 1px solid black; " \
                                f"border-radius: {BORDER_RADIUS};}}"

    REGION_FORECAST_STYLESHEET  = f"#{REGION_FORECAST_NAME}{{" \
                                f"border: 1px solid black; " \
                                f"border-radius: {BORDER_RADIUS};}}"

    REGION_INDOOR_STYLESHEET    = f"#{REGION_INDOOR_NAME}{{" \
                                 f"border: 1px solid black; " \
                                 f"border-radius: {BORDER_RADIUS};}}"


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
    UPDATE_INTERVAL_CURRENT: int    = 1  # 1 hour
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

##########################################################################
# Weather Labels
##########################################################################
HEADER_TEXT_SIZE: int       = 30
DEFAULT_TEXT_SIZE: int      = 25


class lblHeader(QLabel):
    """ Header Label """
    def __init__(self, text, parent=None):
        super(lblHeader, self).__init__(text, parent)
        self.setFont(self._setFont())

    def _setFont(self):
        font = QFont()
        font.setPointSize(HEADER_TEXT_SIZE)
        font.setBold(True)
        return font


class lblText(QLabel):
    """ Default Text Label """
    def __init__(self, text, parent=None):
        super(lblText, self).__init__(text, parent)
        self.setFont(self._setFont())

    def _setFont(self):
        font = QFont()
        font.setPointSize(DEFAULT_TEXT_SIZE)
        return font
