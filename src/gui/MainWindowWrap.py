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
from PyQt4 import QtGui, QtCore, QtSql

from src.gui import MainWindow, ParametersDialog

class MainWindowWrap(QtGui.QMainWindow):
    def __init__(self, dbModel):
        super(self.__class__, self).__init__()
        self.dbModel = dbModel;
        dbModel.setParent(self);
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
        self.ui.searchBar.textChanged.connect(self.searchTextChanged)
        self.ui.tableView.setModel(self.dbModel)

        
    def newEntry(self):
        print('new entry')

    def showParameters(self):
        parameterDialog = ParametersDialog.ParametersDialog(self)
        parameterDialog.show()
        
    def search(self):
        self.ui.searchBar.setFocus()

    def searchTextChanged(self, string):
        if str(string) is '':
            self.dbModel.setFilter('')
        else:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT rowid FROM data_fts WHERE data_fts MATCH :searchstr')
            query.bindValue(':searchstr', "'*"+string+"*'")
            success = query.exec_()

            idFound = []

            while query.next():
                idFound.append(str(query.value(0).toString()))

            self.dbModel.setFilter('rowid IN (%s)' % ','.join(idFound))#protect against injection?


            
        
        
            


        
