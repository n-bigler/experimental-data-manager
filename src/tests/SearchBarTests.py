# -*- coding: utf-8 -*-

import sys
import unittest
import pdb
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
from PyQt4 import QtSql
from ..gui import MainWindowWrap

app = QApplication(sys.argv)

class SearchBarTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(SearchBarTests, cls).setUpClass()
        cls._db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        cls._db.setDatabaseName('src/tests/dataTests.db')
        if not cls._db.open():
            print("Error")


        
    def setUp(self):
        self.db = self.__class__._db
        self.dbModel = QtSql.QSqlTableModel()
        self.dbModel.setTable('data')
        self.dbModel.select()
        self.mainWindow = MainWindowWrap.MainWindowWrap(self.dbModel)


    def test_initialDBRowCounts(self):
        self.assertEqual(self.dbModel.rowCount(), 38)


    def test_notExistingSearch(self):
        self.mainWindow.ui.searchBar.setText("dsfjsldfjafdgsdfgfdsyvcxarewfwa")
        self.assertEqual(self.dbModel.rowCount(), 0)

    def test_partialSearch(self):
        self.mainWindow.ui.searchBar.setText("Ven")
        self.assertEqual(self.dbModel.rowCount(), 7)


if __name__ == "__main__":
    unittest.main()
