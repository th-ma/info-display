# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QGridLayout
from loguru import logger

from configs.config_weather import lblText, lblHeader

WI: int = int(1024 / 3)
HI: int = int(600 / 4)

SPACING: int = 0

STRETCH_LABEL: int = 0
STRETCH_BUTTON: int = 0

MARGIN_LEFT: int = 0
MARGIN_TOP: int = 0
MARGIN_RIGHT: int = 0
MARGIN_BOTTOM: int = 0


class WeatherOutdooor(QWidget):
    def __init__(self, parent=None):
        super(WeatherOutdooor, self).__init__(parent)
        if parent:
            self.setGeometry(0, 0, parent.width(), parent.height())
            self.setFixedSize(parent.width(), parent.height())
        else:
            self.setGeometry(100, 100, WI, HI)
            self.setFixedSize(WI, HI)
        self.lblHeader = lblHeader("Outdoor")

        self.iconCurrent = lblText('')
        self.iconCurrent.setPixmap(self._get_weather_icon('1', self))

        self.lblCurrent = lblText("Wolkig oder so")

        self.iconTemperature = self._get_icon(
            '/home/thomaier/projects/myscreens/info-display/infodisplay/ui/weather/res/temperature.svg',
            self)
        self.lblTemperature = lblText("99,9")
        self.iconTemperatureUnit = self._get_icon(
            '/home/thomaier/projects/myscreens/info-display/infodisplay/ui/weather/res/C.svg', self)

        self.iconHumidity = self._get_icon(
            '/home/thomaier/projects/myscreens/info-display/infodisplay/ui/weather/res/humidity.svg', self)
        self.lblHumidity = lblText("88")
        self.lblHumidityUnit = lblText("%")

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(10, 0, 0, 0)
        # Header, center
        layout.addWidget(self.lblHeader, 0, 0, 1, 6, Qt.AlignHCenter | Qt.AlignTop)
        # Current Weather Icon and  Text
        layout.addWidget(self.iconCurrent, 1, 0, Qt.AlignVCenter | Qt.AlignLeft)
        layout.addWidget(self.lblCurrent, 1, 1, 1, 5, Qt.AlignVCenter | Qt.AlignLeft)
        # Current Temperature
        layout.addWidget(self.iconTemperature, 2, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        layout.addWidget(self.lblTemperature, 2, 1, Qt.AlignVCenter | Qt.AlignLeft)
        layout.addWidget(self.iconTemperatureUnit, 2, 2, Qt.AlignVCenter | Qt.AlignLeft)

        layout.addWidget(self.iconHumidity, 2, 3, Qt.AlignVCenter | Qt.AlignLeft)
        layout.addWidget(self.lblHumidity, 2, 4, Qt.AlignVCenter | Qt.AlignLeft)
        layout.addWidget(self.lblHumidityUnit, 2, 5, Qt.AlignVCenter | Qt.AlignLeft)

        self.setLayout(layout)

    def updateData(self, current):
        logger.info(f'updateData')
        self.iconCurrent.setPixmap(self._get_weather_icon(current[0]['WeatherIcon'], self))
        self.lblCurrent.setText(current[0]['WeatherText'])
        self.lblTemperature.setText(str(current[0]['RealFeelTemperature']['Metric']['Value']))
        self.lblHumidity.setText(str(current[0]['RelativeHumidity']))

    def TestinitUI(self):
        label = QLabel("Label Text")
        button = QPushButton("Button Text")

        layout = QVBoxLayout()
        layout.setSpacing(SPACING)

        layout.setContentsMargins(MARGIN_LEFT,
                                  MARGIN_TOP,
                                  MARGIN_RIGHT,
                                  MARGIN_BOTTOM)
        layout.addWidget(label,
                         STRETCH_LABEL,
                         Qt.AlignTop)
        layout.addWidget(button,
                         STRETCH_BUTTON,
                         Qt.AlignTop)

        self.setLayout(layout)

    ## Helper Functions ##
    def _get_weather_icon(self, id, region):
        path = f'infodisplay/ui/weather/res/{id}.png'
        # path = f'/home/thomaier/projects/myscreens/info-display/infodisplay/ui/weather/res/{id}.png'
        label = lblText('')
        pixmap = QPixmap(path)
        return pixmap

    def _get_icon(self, path, region):
        # path = f'infodisplay/ui/weather/res/{id}.png'
        label = lblText('')
        pixmap = QPixmap(path)
        # pixmap= pixmap.scaled(40,40, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        return label


if __name__ == '__main__':
    app = QApplication([])
    w = WeatherOutdooor()
    w.show()
    app.exec_()
