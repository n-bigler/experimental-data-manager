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

class ParametersDialog(QtGui.QDialog):
    def __init__(self, parent=None, currentPath='.'):
        super(self.__class__, self).__init__()
        QtGui.QDialog.__init__(self, parent)

        self.ui = SelectDatabaseWidget.Ui_ParametersDialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.browseButton.released.connect(self.browse)
        self.currentPath = currentPath;
        # first initialize line edit with current path
        self.ui.databaseURLLineEdit.setText(currentPath)
        # then setup a slot for any edit of line edit
        self.ui.databaseURLLineEdit.textChanged.connect(self.urlChanged)

        #ok and cancel buttons
        self.ui.okCancelButtonBox.accepted.connect(self.submit)
        self.ui.okCancelButtonBox.rejected.connect(self.cancel)

    def urlChanged(self, newURL):
        self.currentPath = newURL


    def browse(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        dialog.setDirectory(self.ui.databaseURLLineEdit.displayText())
        if dialog.exec_():
            files = dialog.selectedFiles()
            self.ui.databaseURLLineEdit.setText(files.first())

            
    def getValues(self):
        return self.currentPath
        
    def submit(self):
        self.accept()
        

    def cancel(self):
        self.reject()

