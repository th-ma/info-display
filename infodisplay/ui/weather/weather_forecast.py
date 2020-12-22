# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout

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

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        # weather text
        layout.addWidget(self.lblText,0,0, Qt.AlignHCenter | Qt.AlignTop)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    w = WeatherForecast()
    w.show()
    app.exec_()
