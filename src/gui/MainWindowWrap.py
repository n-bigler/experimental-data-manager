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
import os
import sqlite3
from PyQt4 import QtGui, QtCore, QtSql

from src.gui import MainWindow, ParametersDialog, EditEntryDialog
from src import Configuration

class MainWindowWrap(QtGui.QMainWindow):
    def __init__(self):
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
        self.ui.searchBar.textChanged.connect(self.searchTextChanged)

        # configuration
        #look in configuration for db address
        self.config = Configuration.Configuration()
        #get the database path set in config
        self.dbPath = self.config.getConfigDB()

        # database
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        # Model for the central table view
        self.dbModel = QtSql.QSqlTableModel(self, self.db)
        self.ui.tableView.setModel(self.dbModel)
        self.ui.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ui.tableView.doubleClicked.connect(self.viewEntry)


        if self.dbPath == "None":
            self.showParameters()
        else:
            self.setDB(self.dbPath)



    def newEntry(self):
        print('new entry')

    def showParameters(self):
        parameterDialog = ParametersDialog.ParametersDialog(self, self.config.getConfigDB())
        if parameterDialog.exec_():
            # I won't end up here if user clicked cancel or the close button of the dialog
            self.setDB(parameterDialog.getValues())

    def search(self):
        self.ui.searchBar.setFocus()

    def searchTextChanged(self, string):
        if str(string) == '':
            self.dbModel.setFilter('')
        else:
            if os.name == 'posix':#for some reason I can't run the QSqlQuery below on OS X.
                conn = sqlite3.connect(self.dbPath)
                curr = conn.cursor()
                curr.execute("SELECT rowid FROM data_fts WHERE data_fts MATCH ?", ("'*"+str(string)+"*'",))
                ids = curr.fetchall()
                idFound = []
                for item in ids:
                    idFound.append(str(item[0]))

                self.dbModel.setFilter('rowid IN (%s)' % ','.join(idFound))#protect against injection?
            else:
                query = QtSql.QSqlQuery()
                #query.prepare("SELECT rowid FROM data_fts WHERE data_fts MATCH :searchstr")
                query.prepare(QtCore.QString("SELECT rowid FROM data_fts WHERE data_fts MATCH :searchstr"))
                query.bindValue(':searchstr', "'*"+string+"*'")
                success=query.exec_()
                print(success)
                idFound = []

                while query.next():
                    idFound.append(str(query.value(0).toString()))

                print(idFound)
                self.dbModel.setFilter('rowid IN (%s)' % ','.join(idFound))#protect against injection?


    def setDB(self, dbURL):
        self.db.setDatabaseName(dbURL)
        if not self.db.open():# fails silently if DB does not exist
            QtGui.QMessageBox.critical(self, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                      "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it."),
                                       QtGui.QMessageBox.Ok)
        else:
            self.dbPath = dbURL
            self.dbModel.setTable('data')
            self.dbModel.select()
            self.updateConfig()

    def updateConfig(self):
        self.config.setConfigDB(self.dbPath)
        self.config.write()


    def viewEntry(self, ind):
        selected = self.ui.tableView.selectionModel().selectedRows()
        self.entryDialog = EditEntryDialog.EditEntryDialog()
        self.entryDialog.retrieveValues(selected[0].data().toString())
        self.entryDialog.displayValues()

        if self.entryDialog.exec_():
            print('accepted')
        else:
            print('rejected')
