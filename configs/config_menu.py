# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum


@dataclass
class ConfigMenu:
    ICON_WIDTH: int = 40
    ICON_HEIGHT: int = ICON_WIDTH  # width and height are the same

    ICON_HOME: str = 'infodisplay/ui/menu/res/home-24px.svg'
    ICON_WEATHER: str = 'infodisplay/ui/menu/res/wb_cloudy-24px.svg'
    ICON_GRILL: str = 'infodisplay/ui/menu/res/outdoor_grill-24px.svg'

    BUTTON_STYLE: str = 'QPushButton{border: 0px solid;}'


class MenuEntry(Enum):
    HOME = 1
    GRILL = 2
    WEATHER = 3
