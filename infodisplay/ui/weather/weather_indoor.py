# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout

from configs.config_weather import lblHeader

WI: int = 300
HI: int = 198


class WeatherIndoor(QWidget):
    def __init__(self, parent=None):
        super(WeatherIndoor, self).__init__(parent)
        if parent:
            self.setGeometry(0, 0, parent.width(), parent.height())
            self.setFixedSize(parent.width(), parent.height())
        else:
            self.setGeometry(100, 100, WI, HI)
            self.setFixedSize(WI, HI)

        self.lblHead = lblHeader('Indoor')

        self.initUI()


    def initUI(self):
        layout = QGridLayout()
        layout.addWidget(self.lblHead, 0,0, Qt.AlignTop | Qt.AlignHCenter)
        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication([])
    w = WeatherIndoor()
    w.show()
    app.exec_()