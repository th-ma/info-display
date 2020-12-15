# -*- coding: utf-8 -*-
from infodisplay.utils.file_utils import does_file_exist, file_get_last_modification_date


class WeatherObject:
    """ Base Class for all weather objects """

    def __init__(self, filename: str, update_cycle: int):
        self.json_file: str
        self.last_update: str = ''
        self.update_needed: bool = False
        self.update_cycle: int = update_cycle

    def _check_file(self, name: str) -> None:
        if does_file_exist(name):
            last_mod = file_get_last_modification_date(name)
            self.last_update = str(last_mod)
            self.json_file = name
        else:
            self.update_needed = True
            self.last_update = None


class WeatherForecast(WeatherObject):
    """ Weather object forecast data """

    def __init__(self, filename: str, update_cycle: int):
        super(WeatherForecast, self).__init__(filename, update_cycle)


class CurrentWeather(WeatherObject):
    """ Weather object current weather data """

    def __init__(self, filename: str, update_cycle: int):
        super(CurrentWeather, self).__init__(filename, update_cycle)