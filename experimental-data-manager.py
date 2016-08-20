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
from PyQt4 import QtGui, QtSql

from src.gui import MainWindowWrap


class ExperimentalDataManager():
    def __init__(self):
        #set up the database
        self.createDB()
        self.dbModel = QtSql.QSqlTableModel()
        self.dbModel.setTable('data')
        self.dbModel.select()
        
        #set up the main window
        self.mainWindow = MainWindowWrap.MainWindowWrap(self.dbModel)
        self.mainWindow.show()


    def createDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.db')
        if not self.db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                     "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it.\n\n" "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)

            return False
        return True
                

def main():
    app = QtGui.QApplication(sys.argv)
    appGui = ExperimentalDataManager()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
