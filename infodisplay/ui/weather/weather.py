# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from loguru import logger

from configs.config_weather import ConfigWeather, lblHeader, lblText
from infodisplay.ui.weather.weather_outdoor import WeatherOutdoor
from infodisplay.ui.weather.weather_thread import WeatherDataThread
from infodisplay.utils.file_utils import get_dict_from_json_file


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
        # read data
        self.forecast = get_dict_from_json_file(ConfigWeather.JSON_WEATHER_FORECAST)
        self.current = get_dict_from_json_file(ConfigWeather.JSON_CURRENT_WEATHER)
        # define regions
        self.region_outdoor = self.createRegionOutdoor()
        self.region_time_date = self.createRegionTimeAndDate()
        self.region_forecast = self.createRegionForecast()
        self.region_indoor = self.createRegionIndoor()
        # update UI
        self.outdoor = WeatherOutdoor(self.region_outdoor)
        self.outdoor.set_data(self.current)
    #    self.updateOutdoorUI()
        #self.setOutdoor()
      #  self.updateForecastUI()
     #   self.updateIndoorUI()
    #    self.updateTimeDateUI()

    def setOutdoor(self):
        # collect data
        header_txt = f'Außen'
        current_temp_txt = str(self.current[0]['Temperature']['Metric']['Value']) + '°C'
        feel_temperature_txt = str(self.current[0]['RealFeelTemperature']['Metric']['Value']) + '°C'
        humidity_txt = self.current[0]['RelativeHumidity']
        weather_text_txt = self.current[0]['WeatherText']
        weather_icon_id = self.current[0]['WeatherIcon']
        weather_icon = self._get_weather_icon(weather_icon_id, self.region_outdoor)
        wind_speed_txt = str(self.current[0]['Wind']['Speed']['Metric']['Value']) + ' ' + \
                             str(self.current[0]['Wind']['Speed']['Metric']['Unit'])
        wind_direction = str(self.current[0]['Wind']['Direction']['Degrees']) + '° aus ' + \
                                 str(self.current[0]['Wind']['Direction']['Localized'])

        vbox = QVBoxLayout(self.region_outdoor)
        h_box = QHBoxLayout()
        t = lblText('Outdoor')
        t.setFixedHeight(22)
        h_box.addWidget(t)

        # current weather
        cw_box = QHBoxLayout()
        cw_box.addWidget(weather_icon)
        cw_box.addStretch(1)
        cw_box.addWidget(lblText(weather_text_txt))
        cw_box.addStretch(2)
        cw_box.setAlignment(Qt.AlignTop)
        h_box.setAlignment(Qt.AlignCenter)
        #
        vbox.addLayout(cw_box)
        vbox.addLayout(h_box)






    def updateOutdoorUI(self):
        logger.info(f'updateOutdoorUI')
        title = lblHeader("Outdoor", self.region_outdoor)
        x = self._get_center_x(title, self.region_outdoor.width())
        title.move(x, 0)
        # prepare data
        current_temperature = lblText(str(self.current[0]['Temperature']['Metric']['Value']) + '°C',
                                      self.region_outdoor)
        feel_temperature = lblText(str(self.current[0]['RealFeelTemperature']['Metric']['Value']) + '°C',
                                   self.region_outdoor)
        humidity = lblText(str(self.current[0]['RelativeHumidity']) + ' %', self.region_outdoor)
        weather_text = lblText(self.current[0]['WeatherText'], self.region_outdoor)
        weather_icon_id = self.current[0]['WeatherIcon']
        weather_icon = self._get_weather_icon(weather_icon_id,self.region_outdoor)
        wind_speed = lblText(str(self.current[0]['Wind']['Speed']['Metric']['Value']) + ' ' +
                             str(self.current[0]['Wind']['Speed']['Metric']['Unit']), self.region_outdoor)
        wind_direction = lblText(str(self.current[0]['Wind']['Direction']['Degrees']) + '° aus ' +
                                 str(self.current[0]['Wind']['Direction']['Localized']),
                                 self.region_outdoor)

        LINE = 40
        weather_icon.move(0, LINE)
        weather_text.move(80, LINE)
        logger.info(weather_icon.width())
        current_temperature.move(self._get_center_x(current_temperature, self.region_outdoor.width()), LINE * 3)
        feel_temperature.move(self._get_center_x(feel_temperature, self.region_outdoor.width()), LINE * 4)
        humidity.move(self._get_center_x(humidity, self.region_outdoor.width()), LINE * 5)
        wind_speed.move(self._get_center_x(wind_speed, self.region_outdoor.width()), LINE * 6)
        wind_direction.move(self._get_center_x(wind_direction, self.region_outdoor.width()), LINE * 7)

        wind = self._get_icon('infodisplay/ui/weather/res/wind.svg', self.region_outdoor)
        wind.move(10,LINE * 9)
        wind.show()



    def updateForecastUI(self):
        title = lblHeader("Forecast", self.region_forecast)
        x = self._get_center_x(title, self.region_forecast.width())
        title.move(x, 0)

    def updateTimeDateUI(self):
        title = lblHeader("Time & Date", self.region_time_date)
        x = self._get_center_x(title, self.region_time_date.width())
        title.move(x, 0)

    def updateIndoorUI(self):
        title = lblHeader("Indoor", self.region_indoor)
        x = self._get_center_x(title, self.region_indoor.width())
        title.move(x, 0)

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

    def _get_weather_icon(self, id, region):
        path = f'infodisplay/ui/weather/res/{id}.png'
        label = lblText('', region)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        return label

    def _get_icon(self, path, region):
        #path = f'infodisplay/ui/weather/res/{id}.png'
        label = lblText('', region)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        return label
