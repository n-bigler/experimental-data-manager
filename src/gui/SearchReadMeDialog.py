
""" TODO: write doc
"""

import sys
from PyQt4 import QtGui, QtCore, QtSql, uic
from src.gui import Ui_SearchReadMeDialog


class SearchReadMeDialog(QtGui.QDialog):
    def __init__(self, parent=None, currentPath='.'):
        super(self.__class__, self).__init__()
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_SearchReadMeDialog.Ui_Ui_SearchReadMeDialog()
        self.ui.setupUi(self)

        self.setModal(True)
        
    def writeLine(self, line):
        self.ui.plainTextEdit.appendPlainText(line)
