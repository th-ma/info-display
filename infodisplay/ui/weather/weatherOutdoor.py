# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPixmap, QFontMetrics
from PyQt5.QtWidgets import QWidget
from loguru import logger

from configs.config_weather import lblText, lblHeader


class WeatherUiOutdoor(QWidget):
    def __init__(self, parent=None):
        super(WeatherUiOutdoor, self).__init__(parent)
        #
        self.lblOutdoorHeader = lblHeader('Outdoor', parent)

        self.iconWeather = self._get_weather_icon_from_id('44')
        self.lblWeatherText = lblText('Bewölkt oder', parent)

        self.iconTemperature = self._get_icon_from_path('infodisplay/ui/weather/res/temperature.svg')
        self.lblCurrentTemperature = lblText('99.9', parent)
        self.iconTemperatureSign = self._get_icon_from_path('infodisplay/ui/weather/res/C.svg')

        self.iconHumidity = self._get_icon_from_path('infodisplay/ui/weather/res/humidity.svg')
        self.lblHumidity = lblText('77', parent)
        self.lblHumidityUnit = lblHeader('%', parent)

        self.calUiPositions()
        # self.initUI()

    def initUI(self):
        logger.info(f'initUI')
        self._position_lblOutdoorHeader()

    def calUiPositions(self):
        self.lblOutdoorHeader.move(self._centerText_h(self.lblOutdoorHeader),
                                   0)
        y_row2 = self.lblOutdoorHeader.height() + int(self.iconWeather.height() / 2)
        self.iconWeather.move(0, y_row2)
        self.lblWeatherText.move(self.iconWeather.width(), y_row2)

        y_row3 = y_row2 + self.iconWeather.height() + int(self.iconTemperature.height() / 2)
        self.iconTemperature.move(10, y_row3)
        logger.info(f'iconTemperature: {self.iconTemperature.width()}')
        self.lblCurrentTemperature.move(52, y_row3)
        self.iconTemperatureSign.move(52 +
                                       self._get_textWidth(self.lblCurrentTemperature),
                                        y_row3)
        y_row4 = y_row2 + y_row3
        self.iconHumidity.move(10, y_row4)
        self.lblHumidity.move(42, y_row4)
        self.lblHumidityUnit.move(42 + self._get_textWidth(self.lblHumidity), y_row4)


    def updateData(self):
        pass

    #### Helper functions
    def _get_weather_icon_from_id(self, id):
        path = f'infodisplay/ui/weather/res/{id}.png'
        label = lblText('', self)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        return label

    def _get_icon_from_path(self, path):
        label = lblText('', self)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        return label

    def _position_lblOutdoorHeader(self):
        w = self.iconWeather.width()
        self.iconWeather.move(int((self.parent().width() - w) / 2), 1)

    def _centerText_h(self, lbl):
        fm = QFontMetrics(lbl.font())
        font_width = fm.width(lbl.text())
        x = self.parent().width() - font_width
        x = x / 2
        #logger.info(f'x {x}')
        return x

    def _get_textWidth(self, lbl):
        fm = QFontMetrics(lbl.font())
        font_width = fm.width(lbl.text())
        return font_width

    def _centerIcon_h(self, icon):
        width = icon.width()
        x = self.parent().width() - width
        x = x / 2
        return x
