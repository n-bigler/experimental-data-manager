#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys
from PyQt4 import QtGui

from src.gui import MainWindowWrap

class ExperimentalDataManager():
    def __init__(self):
        self.mainWindow = MainWindowWrap.MainWindowWrap()
        self.mainWindow.show()

def main():
    app = QtGui.QApplication(sys.argv)
    appGui = ExperimentalDataManager()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
