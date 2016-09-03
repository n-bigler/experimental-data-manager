#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Application entry point

Calls up the main window.
"""

import sys
import pdb
from PyQt4 import QtGui, QtSql

from src.gui import MainWindow



class ExperimentalDataManager():
    def __init__(self):
        #set up the database


        #set up the main window
        self.mainWindow = MainWindow.MainWindow()
        self.mainWindow.show()




def main():
    app = QtGui.QApplication(sys.argv)
    appGui = ExperimentalDataManager()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
