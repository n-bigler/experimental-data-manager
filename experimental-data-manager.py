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
from PyQt4 import QtGui, QtCore

from src.gui import MainWindow, ParametersDialog

class ExperimentalDataManager(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.actionNew_Entry.setShortcut('Ctrl+N')
        self.actionNew_Entry.triggered.connect(self.newEntry)
        self.actionParameters.setShortcut('Ctrl+K')
        self.actionParameters.triggered.connect(self.showParameters)
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.searchBar = QtGui.QLineEdit(self)
        self.toolBar.addWidget(self.searchBar)
        self.actionSearch.triggered.connect(self.search)
        

        
    def newEntry(self):
        print('new entry')

    def showParameters(self):
        parameterDialog = ParametersDialog.ParametersDialog(self)
        parameterDialog.show()
        
    def search(self):
        self.searchBar.setFocus()

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    mainWindow = ExperimentalDataManager()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
