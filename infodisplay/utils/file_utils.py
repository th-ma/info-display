# -*- coding: utf-8 -*-
import json
import pathlib
from datetime import datetime

from loguru import logger


def does_file_exist(filename: str) -> bool:
    """
        Checks if file exist
        :parameter filename as string
        :return True if file exist, otherwise False
    """
    retVal: bool = False
    file = pathlib.Path(filename)
    if file.is_file():
        retVal = True
    return retVal


def file_get_last_modification_date(filename: str):
    file = pathlib.Path(filename)
    modificationTime = datetime.fromtimestamp(file.stat().st_mtime)
    return str(modificationTime)


####################  JSON ###############################
def save_jsondata_2_jsonfile(filename: str, data: dict) -> None:
    """ save dictionary data to given file """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data,
                      file,
                      ensure_ascii=False,
                      indent=4)
    except IOError as e:
        logger.error(f'I/O Error: {e.errno, e.strerror}')


def dump_dict2json_file(filename: str, dic: dict) -> None:
    """ store dictionary in file """
    try:
        with open(filename, 'w') as file:
            json.dump(dic, file)
    except IOError as e:
        logger.error(f'"I/O Error: {e.errno, e.strerror}')


def get_dict_from_json_file(filename: str):
    """ reads and returns dict from given json file """
    try:
        with open(filename, 'r') as file:
            dic = json.load(file)
            return dic
    except IOError as e:
        logger.error(f'"I/O Error: {e.errno, e.strerror}')
        return None


def mqtt_send_json_file(filename: str):
    send = get_dict_from_json_file(filename)
    data = json.dumps(send)
    return data
