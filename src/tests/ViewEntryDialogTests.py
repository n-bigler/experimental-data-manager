# -*- coding: utf-8 -*-

import sys
import unittest
import pdb
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
from PyQt4 import QtSql, QtCore
from ..gui import MainWindowWrap
from ..gui import EditEntryDialog



class ViewEntryDialogTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(ViewEntryDialogTests, cls).setUpClass()
        cls._mainWindow = MainWindowWrap.MainWindowWrap()
        cls._mainWindow.setDB('src/tests/dataTests.db')



    def test_viewEntry(self):
        # first select row with id 4
        rowPos = self._mainWindow.ui.tableView.rowViewportPosition(3)
        QTest.mouseClick(self._mainWindow.ui.tableView.viewport(), Qt.LeftButton, Qt.NoModifier, QtCore.QPoint(0, rowPos))

        # then make sure we are selecting the correct row
        self.assertEqual(str(self._mainWindow.getSelectedRow()), "4")

        #now we check that the dialog has the correct entries
        entryDialog = EditEntryDialog.EditEntryDialog()
        entryDialog.retrieveValues("4")
        entryDialog.displayValues()
        self.assertEqual(str(entryDialog.ui.projectLineEdit.text()), "OPCPA E4")
        # should maybe test the other texts info in the dialog

if __name__ == "__main__":
    unittest.main()

