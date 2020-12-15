# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil import parser


def get_time_diff_from_date_string(date_str: str):
    """ returns the time difference in hours """
    if date_str =='':
        date = datetime.now()
    else:
        date = parser.parse(date_str)
    now = datetime.now()
    diff = now - date
    # convert diff to hours
    delta_hours = divmod(diff.total_seconds(), 3600)[0]
    return delta_hours


def get_now_as_string() -> str:
    """" returns datetime now as a string """
    now = datetime.now()
    return str(now)
