# -*- coding: utf-8 -*-
import argparse
import threading
import time

from PyQt5.QtWidgets import QApplication
from loguru import logger
from qt_material import apply_stylesheet

from infodisplay.gui import MainWindow
from infodisplay.server.weatherServer.weather_server import WeatherServer


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', action="store_true")
    args = vars(ap.parse_args())
    if args['s']:
        start_weather_server()
    else:
        start_app()


def start_app():
    app = QApplication([])
    # qt-material style sheet
    apply_stylesheet(app, theme='dark_teal.xml')
    w = MainWindow()
    w.show()
    app.exec_()


def start_weather_server():
    logger.debug(f'start_weather_server()')
    run_event = threading.Event()
    run_event.set()
    # get device threads
    dev = WeatherServer(1, run_event)
    dev.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.error(f'Signaling all device threads to finish')
        run_event.clear()
        dev.join()
        logger.error(f'All threads finished, exiting')


if __name__ == '__main__':
    #start_weather_server()
    main()
