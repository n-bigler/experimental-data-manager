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

class MainWindowWrap(QtGui.QMainWindow):
    def __init__(self, dbModel):
        super(self.__class__, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew_Entry.setShortcut('Ctrl+N')
        self.ui.actionNew_Entry.triggered.connect(self.newEntry)
        self.ui.actionParameters.setShortcut('Ctrl+K')
        self.ui.actionParameters.triggered.connect(self.showParameters)
        self.ui.actionQuit.setShortcut('Ctrl+Q')
        self.ui.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.ui.searchBar = QtGui.QLineEdit(self.ui.toolBar)
        self.ui.toolBar.addWidget(self.ui.searchBar)
        self.ui.actionSearch.triggered.connect(self.search)
        self.ui.tableView.setModel(dbModel)

        
    def newEntry(self):
        print('new entry')

    def showParameters(self):
        parameterDialog = ParametersDialog.ParametersDialog(self)
        parameterDialog.show()
        
    def search(self):
        self.ui.searchBar.setFocus()

        
