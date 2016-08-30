# -*- coding: utf-8 -*-

import sys
import unittest
import pdb
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
from PyQt4 import QtSql
from ..gui import MainWindowWrap



class SearchBarTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        super(SearchBarTests, cls).setUpClass()
        cls._mainWindow = MainWindowWrap.MainWindowWrap()
        cls._mainWindow.setDB('src/tests/dataTests.db')



    def test_initialDBRowCounts(self):
        self.assertEqual(self._mainWindow.dbModel.rowCount(), 38)


    def test_notExistingSearch(self):
        self._mainWindow.ui.searchBar.setText("dsfjsldfjafdgsdfgfdsyvcxarewfwa")
        self.assertEqual(self._mainWindow.dbModel.rowCount(), 0)

    def test_partialSearch(self):
        self._mainWindow.ui.searchBar.setText("Ven")
        self.assertEqual(self._mainWindow.dbModel.rowCount(), 7)


if __name__ == "__main__":
    unittest.main()
