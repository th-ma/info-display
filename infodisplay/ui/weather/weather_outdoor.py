# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout
from loguru import logger

from configs.config_weather import lblText, lblHeader


class WeatherOutdoor(QWidget):
    def __init__(self, parent=None):
        super(WeatherOutdoor, self).__init__(parent)
        self.regionCurrent = self._set_currentRegion()
        self.regionTemperature = self._set_temperatureRegion()
        self.regionHumidity = self._setHumidityRegion()

    def currentData(self):
        layout = QHBoxLayout(self.regionCurrent)
        weather_icon_id = self.weather_data[0]['WeatherIcon']
        weather_icon = self._get_weather_icon(weather_icon_id, self.regionCurrent)
        weather_text_txt = self.weather_data[0]['WeatherText']
        layout.addWidget(weather_icon)
        layout.addStretch(1)
        layout.addWidget(lblText(weather_text_txt))
        layout.addStretch(2)
        self.regionCurrent.setLayout(layout)

    def setHumidityData(self):
        layout = QHBoxLayout(self.regionHumidity)
        h_icon = self._get_icon('infodisplay/ui/weather/res/humidity.svg', self.regionHumidity)
        h_text = str(self.weather_data[0]['RelativeHumidity']) + ' %'
        layout.addWidget(h_icon)
        layout.addStretch(1)
        layout.addWidget(lblText(h_text))
        layout.addStretch(2)
        self.regionHumidity.setLayout(layout)

    def setTemperatureData(self):
        layout = QHBoxLayout(self.regionTemperature)
        temp_icon = self._get_icon('infodisplay/ui/weather/res/temperature.svg', self.regionTemperature)
        c_icon = self._get_icon('infodisplay/ui/weather/res/C.svg', self.regionTemperature)
        current_temp_txt = str(self.weather_data[0]['Temperature']['Metric']['Value'])
        feel_temp_text = str(self.weather_data[0]['RealFeelTemperature']['Metric']['Value']) + ' Gefühlt'
        # current_temp_txt = f'\t{current_temp_txt}\n{feel_temp_text}'
        layout.addWidget(temp_icon)
        layout.addStretch(1)
        layout.addWidget(lblHeader(current_temp_txt))
        layout.addStretch(1)
        layout.addWidget(c_icon)
        layout.addStretch(1)
        # layout.setAlignment(Qt.AlignVCenter)
        self.regionTemperature.setLayout(layout)

    def set_data(self, data: dict):
        self.weather_data = data
        self.currentData()
        self.setTemperatureData()
        self.setHumidityData()

    def _get_icon(self, path, region):
        # path = f'infodisplay/ui/weather/res/{id}.png'
        label = lblText('', region)
        pixmap = QPixmap(path)
        #pixmap= pixmap.scaled(40,40, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        return label

    def _get_weather_icon(self, id, region):
        path = f'infodisplay/ui/weather/res/{id}.png'
        label = lblText('', region)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        return label

    def _set_currentRegion(self):
        regionCurrent = QFrame(self)
        regionCurrent.setGeometry(0, 0, self.parent().width(), 60)
        regionCurrent.setObjectName("cur")
        style = '#cur {border: 0px solid black; background-color: transparent;}'
        regionCurrent.setStyleSheet(style)
        return regionCurrent

    def _set_temperatureRegion(self):
        regionTemperature = QFrame(self)
        regionTemperature.setGeometry(0, self.regionCurrent.height(), self.parent().width(), 80)
        regionTemperature.setObjectName("rtemp")
        style = '#rtemp {border: 0px solid black; background-color: transparent;}'
        regionTemperature.setStyleSheet(style)
        return regionTemperature

    def _setHumidityRegion(self):
        regionHumidity = QFrame(self)
        regionHumidity.setGeometry(0, self.regionCurrent.height() + self.regionTemperature.height(),
                                   self.parent().width(), 50)
        regionHumidity.setObjectName("rhum")
        style = '#rhum {border: 0px solid black; background-color: transparent;}'
        regionHumidity.setStyleSheet(style)
        return regionHumidity
