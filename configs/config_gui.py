# -*- coding: utf-8 -*-
from dataclasses import dataclass

"""
    GUI configurations for MainWindow
"""


@dataclass
class ConfigGui:
    ''' Physical config '''
    DISPLAY_WIDTH: int  = 1024
    DISPLAY_HEIGHT: int = 600
    TOUCH_ENABLED: bool = True

    ''' Background config '''
    BACKGROUND_OBJECT_NAME: str = 'backGround'
    BACKGROUND_STYLE_SHEET: str = f'#{BACKGROUND_OBJECT_NAME} {{' \
                                  f' background-color: grey;}}'

    ''' Foreground config'''
    FOREGROUND_OBJECT_NAME: str = 'foreGround'
    # set FG
    FOREGROUND_STYLE_SHEET: str = f'#{FOREGROUND_OBJECT_NAME} {{' \
                                  f' background-color: transparent;}}'

    ''' REGIONS CONFIG '''
    POS_X: int              = 0                                 # same for all regions
    WIDTH: int              = DISPLAY_WIDTH                     # same for all regions
    # Menu Bar
    MENU_BAR_POS_X: int     = POS_X
    MENU_BAR_POS_Y: int     = 0                                 # start at top of screen
    MENU_BAR_WIDTH: int     = WIDTH
    MENU_BAR_HEIGHT: int    = 50
    MENU_BAR_NAME: str      = 'menu_bar'
    # CONTENT
    CONTENT_POS_X: int      = POS_X
    CONTENT_POS_Y: int      = POS_X + MENU_BAR_HEIGHT           # start at bottom of menu bar
    CONTENT_WIDTH: int      = WIDTH
    CONTENT_HEIGHT: int     = 500                               #
    CONTENT_NAME: str       = 'content'
    # status bar
    STATUS_BAR_POS_X: int   = POS_X
    STATUS_BAR_POS_Y: int   = CONTENT_POS_Y + CONTENT_HEIGHT    # start at bottom of content
    STATUS_BAR_WIDTH: int   = WIDTH
    STATUS_BAR_HEIGHT: int  = 50
    STATUS_BAR_NAME: str    = 'status_bar'
