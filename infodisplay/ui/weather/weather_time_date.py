# -*- coding: utf-8 -*-
from time import strftime

from PyQt5.QtCore import Qt, QTimer, QDate
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLCDNumber, QVBoxLayout, QHBoxLayout, QLabel

from configs.config_weather import lblText

WI: int = 400
HI: int = 198


class WeatherTimeDate(QWidget):
    def __init__(self, parent=None):
        super(WeatherTimeDate, self).__init__(parent)
        if parent:
            self.setGeometry(0, 0, parent.width(), parent.height())
            self.setFixedSize(parent.width(), parent.height())
        else:
            self.setGeometry(100, 100, WI, HI)
            self.setFixedSize(WI, HI)

        self.lblDate = lblText('12.12.2021')
        self.lblTime = QLCDNumber()
        self.lblTime.setStyleSheet('border: 0px;')
        self.lblLocation = lblText('Sontheim an der Brenz')

        self.timer = QTimer()
        self.timer.timeout.connect(self._updateTime)
        self.timer.start(1000)
        self._configureClock()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, -1, 0, -1)

        layout.addWidget(self.lblTime, Qt.AlignHCenter | Qt.AlignTop)

        up = '\u2191'
        down = '\u2193'

        hlayout = QHBoxLayout()
        hlayout.setSpacing(0)
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.addWidget(self.lblDate, Qt.AlignLeft | Qt.AlignBottom)
        hlayout.addWidget(QLabel(f'\n{up}: 11:23\n{down}: 23:00'))  # ,Qt.AlignRight | Qt.AlignBottom)

        layout.addLayout(hlayout, Qt.AlignBottom)

        self.setLayout(layout)

    def _configureClock(self):
        self.lblTime.setNumDigits(5)
        self.lblTime.setMinimumHeight(60)
        self.lblTime.setSegmentStyle(2)

    def _updateTime(self):
        self.lblTime.display(strftime("%H" + ":" + "%M"))
        date = QDate.currentDate().toString("dddd\ndd.MMMM yyyy")
        self.lblDate.setText(date)


if __name__ == '__main__':
    app = QApplication([])
    w = WeatherTimeDate()
    w.show()
    app.exec_()
