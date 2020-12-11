# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSize, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from loguru import logger

from configs.config_menu import ConfigMenu, MenuEntry


class Menu(QWidget):
    menuSignal = pyqtSignal(int)

    def __init__(self, cb, parent=None):
        super(Menu, self).__init__(parent)
        if parent:
            self.setFixedSize(parent.width(), parent.height())
        self.initUI()
        self.callback_menu = cb

    def initUI(self):
        layout = QHBoxLayout()
        iconSize = QSize(ConfigMenu.ICON_WIDTH,
                         ConfigMenu.ICON_HEIGHT)
        style_sheet = ConfigMenu.BUTTON_STYLE
        ''' home button '''
        btHome = QPushButton()
        homeIcon = QIcon(ConfigMenu.ICON_HOME)
        btHome.setIcon(homeIcon)
        btHome.setIconSize(iconSize)
        btHome.setStyleSheet(style_sheet)
        btHome.clicked.connect(self.on_home_clicked)

        ''' Grill '''
        btGrill = QPushButton()
        grillIcon = QIcon(ConfigMenu.ICON_GRILL)
        btGrill.setIcon(grillIcon)
        btGrill.setIconSize(iconSize)
        btGrill.setStyleSheet(style_sheet)
        btGrill.clicked.connect(self.on_grill_clicked)

        '''' Weather '''
        btWeather = QPushButton()
        weatherIcon = QIcon(ConfigMenu.ICON_WEATHER)
        btWeather.setIcon(weatherIcon)
        btWeather.setIconSize(iconSize)
        btWeather.setStyleSheet(style_sheet)
        btWeather.clicked.connect(self.on_weather_clicked)

        layout.addWidget(btHome)
        layout.addWidget(btGrill)
        layout.addWidget(btWeather)

        self.setLayout(layout)

    @pyqtSlot()
    def on_home_clicked(self):
        self.callback_menu(MenuEntry.HOME)

    @pyqtSlot()
    def on_grill_clicked(self):
        self.callback_menu(MenuEntry.GRILL)

    @pyqtSlot()
    def on_weather_clicked(self):
        self.callback_menu(MenuEntry.WEATHER)
