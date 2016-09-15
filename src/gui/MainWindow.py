# -*- coding: utf-8 -*-

"""The main app window

Manages most of the events as well as the connection to the DB.
"""

from __future__ import unicode_literals
import sys
import pdb
import os
import glob
import fnmatch
import sqlite3
import re
from PyQt4 import QtGui, QtCore, QtSql

from src.gui import Ui_MainWindow, ParametersDialog, EditEntryDialog, SyncRootFolderDialog, SearchReadMeDialog
from src import Configuration

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew_Entry.setShortcut('Ctrl+N')
        self.ui.actionNew_Entry.triggered.connect(self.newEntry)
        self.ui.actionParameters.setShortcut('Ctrl+K')
        self.ui.actionParameters.triggered.connect(self.showParameters)
        self.ui.actionQuit.setShortcut('Ctrl+Q')
        self.ui.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.ui.toolBar.addAction(self.ui.actionSync)
        self.ui.actionSync.setIcon(QtGui.QIcon("icons/sync.png")) # TODO: Shouldn't this be set by the designer?
        self.ui.searchBar = QtGui.QLineEdit(self.ui.toolBar)
        self.ui.toolBar.addWidget(self.ui.searchBar)
        self.ui.actionSearch.triggered.connect(self.search)
        self.ui.searchBar.textChanged.connect(self.searchTextChanged)
        self.ui.actionSync.triggered.connect(self.showSyncRootFolderDialog)


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
            if  sys.platform != 'linux2':#for some reason I can't run the QSqlQuery below on OS X.
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


    def getSelectedRow(self):
        selected = self.ui.tableView.selectionModel().selectedRows()
        return selected[0].data().toString()



    def viewEntry(self, ind):
        entryDialog = EditEntryDialog.EditEntryDialog()
        rowID = self.getSelectedRow()
        entryDialog.retrieveValues(rowID)
        entryDialog.displayValues()

        if entryDialog.exec_():
            newProject = entryDialog.ui.projectLineEdit.text()
            self.updateDB(newProject, rowID)


    def updateDB(self, newProject, id):
        query = QtSql.QSqlQuery()
        sqlQuery = QtCore.QString("UPDATE data SET project=:project WHERE id=:id")
        query.prepare(sqlQuery)
        query.bindValue(':project', newProject)
        query.bindValue(':id', id)
        query.exec_()
        query.lastQuery()
        self.dbModel.submitAll()
        self.dbModel.select()

    def showSyncRootFolderDialog(self):
        syncRFDialog = SyncRootFolderDialog.SyncRootFolderDialog(self)
        if syncRFDialog.exec_():
            # I won't end up here if user clicked cancel or the close button of the dialog
            self.searchReadMe(syncRFDialog.getValues())


    def searchReadMe(self, rootFolder):
        dialog = SearchReadMeDialog.SearchReadMeDialog(self, rootFolder)
        dialog.exec_()
        entriesFound = dialog.getValues()
        for entry in entriesFound:
            self.addToDB(entry)

    def addToDB(self, dat):
        query = QtSql.QSqlQuery()
        query.prepare(QtCore.QString("SELECT id FROM data WHERE path=:path"))
        print(dat['path'])
        query.bindValue(':path', dat['path'])
        query.exec_()
        idFound = []

        while query.next():
            idFound.append(str(query.value(0).toString()))
        print(idFound)
        
        entry = (dat['Date'], dat['Project'], dat['path'], dat['Measurement'], dat['Comment']) # already unicode
        # we check if the record exists in the DB
        if len(idFound) == 0:
            # we write a new record to the DB
            query = QtSql.QSqlQuery()
            sqlQuery = QtCore.QString("INSERT INTO data(date, project, path, measurement, comment) VALUES (:date,:project,:path,:measurement,:comment)")
            query.prepare(sqlQuery)
            query.bindValue(':date', dat['Date'])
            query.bindValue(':project', dat['Project'])
            query.bindValue(':path', dat['path'])
            query.bindValue(':measurement', dat['Measurement'])
            query.bindValue(':comment', dat['Comment'])
            query.exec_()
            print("Added to DB: ")
            print(dat)


        else:
            # we need to update one record
            query = QtSql.QSqlQuery()
            sqlQuery = QtCore.QString("UPDATE data SET date=:date, project=:project, measurement=:measurement, comment=:coment WHERE id=:id")
            query.prepare(sqlQuery)
            query.bindValue(':date', dat['Date'])
            query.bindValue(':project', dat['Project'])
            query.bindValue(':path', dat['path'])
            query.bindValue(':measurement', dat['Measurement'])
            query.bindValue(':comment', dat['Comment'])
            query.exec_()
            print("Updated: ")
            print(dat)

