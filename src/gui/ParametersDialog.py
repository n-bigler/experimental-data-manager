#!/usr/bin/python

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
from src.gui import SelectDatabaseWidget

class ParametersDialog(QtGui.QDialog, SelectDatabaseWidget.Ui_ParametersDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        self.browseButton.released.connect(self.browse)

    def browse(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')


