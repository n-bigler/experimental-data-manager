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
import pdb
from PyQt4 import QtGui, QtSql

from src.gui import MainWindowWrap



class ExperimentalDataManager():
    def __init__(self):
        #set up the database

        
        #set up the main window
        self.mainWindow = MainWindowWrap.MainWindowWrap()
        self.mainWindow.show()


                

def main():
    app = QtGui.QApplication(sys.argv)
    appGui = ExperimentalDataManager()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
