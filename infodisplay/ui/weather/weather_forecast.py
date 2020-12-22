# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QHBoxLayout, QVBoxLayout

from configs.config_weather import lblText

WI: int = 1004
HI: int = 298


class WeatherForecast(QWidget):
    def __init__(self, parent=None):
        super(WeatherForecast, self).__init__(parent)
        if parent:
            self.setGeometry(0, 0, parent.width(), parent.height())
            self.setFixedSize(parent.width(), parent.height())
        else:
            self.setGeometry(100, 100, WI, HI)
            self.setFixedSize(WI, HI)
        # define labels
        self.lblText = lblText('Voraussichtlich Scheißwetter Montagabend bis Dienstagnachmittag')
        # day 0 - today
        self.lblDate_day0 = QLabel('01.01.20')
        self.lblMax_day0 = QLabel('22°C')
        self.lblMin_day0 = QLabel('-2°C')
        self.lblIcon_day0 = QLabel('')
        self.lblIcon_day0.setPixmap(self._getPixmap_from_id('1'))
        self.lblSunHours_day0 = QLabel('0h')
        self.lblPrecipitation_day0 = QLabel('1h')

        self.lblDate_day1 = QLabel('02.01.20')
        self.lblMax_day1 = QLabel('22°C')
        self.lblMin_day1 = QLabel('-2°C')
        self.lblIcon_day1 = QLabel('')
        self.lblIcon_day1.setPixmap(self._getPixmap_from_id('2'))
        self.lblSunHours_day1 = QLabel('0h')
        self.lblPrecipitation_day1 = QLabel('1h')

        self.lblDate_day2 = QLabel('03.01.20')
        self.lblMax_day2 = QLabel('22°C')
        self.lblMin_day2 = QLabel('-2°C')
        self.lblIcon_day2 = QLabel('')
        self.lblIcon_day2.setPixmap(self._getPixmap_from_id('3'))
        self.lblSunHours_day2 = QLabel('0h')
        self.lblPrecipitation_day2 = QLabel('1h')

        self.lblDate_day3 = QLabel('04.01.20')
        self.lblMax_day3 = QLabel('22°C')
        self.lblMin_day3 = QLabel('-2°C')
        self.lblIcon_day3 = QLabel('')
        self.lblIcon_day3.setPixmap(self._getPixmap_from_id('4'))
        self.lblSunHours_day3 = QLabel('0h')
        self.lblPrecipitation_day3 = QLabel('1h')

        self.init2UI()

    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        # weather text
        layout.addWidget(self.lblText, 0, 0, 1, 4, Qt.AlignHCenter | Qt.AlignTop)

        layout.addWidget(self.lblDate_day0, 1, 0, Qt.AlignHCenter)
        layout.addWidget(self.lblDate_day1, 1, 1, Qt.AlignHCenter)
        layout.addWidget(self.lblDate_day2, 1, 2, Qt.AlignHCenter)
        layout.addWidget(self.lblDate_day3, 1, 3, Qt.AlignHCenter)

        layout.addWidget(self.lblMax_day0, 2, 0, Qt.AlignHCenter)
        layout.addWidget(self.lblMax_day1, 2, 1, Qt.AlignHCenter)
        layout.addWidget(self.lblMax_day2, 2, 2, Qt.AlignHCenter)
        layout.addWidget(self.lblMax_day3, 2, 3, Qt.AlignHCenter)

        layout.addWidget(self.lblMin_day0, 3, 0, Qt.AlignHCenter)
        layout.addWidget(self.lblMin_day1, 3, 1, Qt.AlignHCenter)
        layout.addWidget(self.lblMin_day2, 3, 2, Qt.AlignHCenter)
        layout.addWidget(self.lblMin_day3, 3, 3, Qt.AlignHCenter)

        self.setLayout(layout)

    def init2UI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.lblText, 0, Qt.AlignTop | Qt.AlignHCenter)

        hcontainer = QHBoxLayout()

        day0_layout = QVBoxLayout()
        day0_layout.addWidget(self.lblDate_day0)
        day0_layout.addWidget(self.lblMax_day0)
        day0_layout.addWidget(self.lblMin_day0)
        day0_layout.addWidget(self.lblIcon_day0)

        day1_layout = QVBoxLayout()
        day1_layout.addWidget(self.lblDate_day1)
        day1_layout.addWidget(self.lblMax_day1)
        day1_layout.addWidget(self.lblMin_day1)
        day1_layout.addWidget(self.lblIcon_day1)

        day2_layout = QVBoxLayout()
        day2_layout.addWidget(self.lblDate_day2)
        day2_layout.addWidget(self.lblMax_day2)
        day2_layout.addWidget(self.lblMin_day2)
        day2_layout.addWidget(self.lblIcon_day2)

        day3_layout = QVBoxLayout()
        day3_layout.addWidget(self.lblDate_day3)
        day3_layout.addWidget(self.lblMax_day3)
        day3_layout.addWidget(self.lblMin_day3)
        day3_layout.addWidget(self.lblIcon_day3)

        hcontainer.addLayout(day0_layout)
        hcontainer.addLayout(day1_layout)
        hcontainer.addLayout(day2_layout)
        hcontainer.addLayout(day3_layout)
        layout.addLayout(hcontainer)
        self.setLayout(layout)


    ## helper functions
    def _getPixmap_from_id(self, id):
        path = f'infodisplay/ui/weather/res/{id}.png'
        pixmap = QPixmap(path)
        return pixmap


if __name__ == '__main__':
    app = QApplication([])
    w = WeatherForecast()
    w.show()
    app.exec_()
