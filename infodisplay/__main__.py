# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication

from infodisplay.gui import MainWindow


def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
