# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame

from configs.config_gui import ConfigGui


def initMenuBar(foreGround: QFrame) -> QFrame:
    region_menu_bar = QFrame(foreGround)
    region_menu_bar.setObjectName(ConfigGui.MENU_BAR_NAME)
    region_menu_bar.setGeometry(ConfigGui.MENU_BAR_POS_X,
                                ConfigGui.MENU_BAR_POS_Y,
                                ConfigGui.MENU_BAR_WIDTH,
                                ConfigGui.MENU_BAR_HEIGHT)
    region_menu_bar.setStyleSheet(f'#{ConfigGui.MENU_BAR_NAME} '
                                  f'{{background-color: transparent;}}')
    return region_menu_bar


def initContent(foreGround) -> QFrame:
    region_content = QFrame(foreGround)
    region_content.setObjectName(ConfigGui.CONTENT_NAME)
    region_content.setGeometry(ConfigGui.CONTENT_POS_X,
                               ConfigGui.CONTENT_POS_Y,
                               ConfigGui.CONTENT_WIDTH,
                               ConfigGui.CONTENT_HEIGHT)
    region_content.setStyleSheet(f'#{ConfigGui.CONTENT_NAME} '
                                 f'{{background-color: transparent;}}')
    return region_content


def initStatusBar(foreGround):
    region_status_bar = QFrame(foreGround)
    region_status_bar.setObjectName(ConfigGui.STATUS_BAR_NAME)
    region_status_bar.setGeometry(ConfigGui.STATUS_BAR_POS_X,
                                  ConfigGui.STATUS_BAR_POS_Y,
                                  ConfigGui.STATUS_BAR_WIDTH,
                                  ConfigGui.STATUS_BAR_HEIGHT)
    region_status_bar.setStyleSheet(f'#{ConfigGui.STATUS_BAR_NAME} '
                                    f'{{background-color: transparent;}}')
    return region_status_bar


def initForeGround(backGround: QFrame) -> QFrame:
    foreGround = QFrame(backGround)
    foreGround.setObjectName(ConfigGui.FOREGROUND_OBJECT_NAME)
    foreGround.setStyleSheet(ConfigGui.FOREGROUND_STYLE_SHEET)
    # full screen size
    foreGround.setGeometry(0, 0,
                           ConfigGui.DISPLAY_WIDTH,
                           ConfigGui.DISPLAY_HEIGHT)
    return foreGround


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initScreen()
        backGround: QFrame = self.initBackGround()
        foreGround: QFrame = initForeGround(backGround)
        # regions
        self.region_menu_bar: QFrame = initMenuBar(foreGround)
        self.region_content: QFrame = initContent(foreGround)
        self.region_status_bar: QFrame = initStatusBar(foreGround)

    def initBackGround(self) -> QFrame:
        backGround = QFrame(self)
        backGround.setObjectName(ConfigGui.BACKGROUND_OBJECT_NAME)
        backGround.setStyleSheet(ConfigGui.BACKGROUND_STYLE_SHEET)
        # full screen size
        backGround.setGeometry(0, 0,
                               ConfigGui.DISPLAY_WIDTH,
                               ConfigGui.DISPLAY_HEIGHT)
        return backGround

    def initScreen(self):
        # set full screen
        self.setFixedSize(ConfigGui.DISPLAY_WIDTH,
                          ConfigGui.DISPLAY_HEIGHT)
        # frameless window
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

    def addUiWidget(self):
        pass
