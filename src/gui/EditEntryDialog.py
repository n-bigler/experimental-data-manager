# -*- coding: utf-8 -*-

"""The edit entry dialog

Shows a specific database entry and allows the user to modify it. It doesn't
write to the database on its own but simply returns the new entry values.

"""
import sys
import subprocess
from PyQt4 import QtGui, QtCore, QtSql
from src.gui import Ui_ViewEntryDialog


class EditEntryDialog(QtGui.QDialog):
    def __init__(self, parent=None, currentPath='.'):
        super(self.__class__, self).__init__()
        QtGui.QDialog.__init__(self, parent)

        self.ui = Ui_ViewEntryDialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.submit)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Discard).clicked.connect(self.cancel)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Open).clicked.connect(self.openFolder)
        self.date = ""
        self.project = ""
        self.path = ""
        self.measurement = ""
        self.comment = ""
        self.displayValues()
        self.setModal(True)


    def retrieveValues(self, rowid):

        query = QtSql.QSqlQuery()
        query.prepare('SELECT date, project, path, measurement, comment  FROM data WHERE rowid=:id')
        query.bindValue(':id', rowid)
        success = query.exec_()

        while (query.next()):
            self.date = query.value(0).toString()
            self.project = query.value(1).toString()
            self.path = query.value(2).toString()
            self.measurement = query.value(3).toString()
            self.comment = query.value(4).toString()


    def displayValues(self):
        self.ui.projectLineEdit.setText(self.project)
        self.ui.dateLineEdit.setText(self.date)
        self.ui.measurementTextEdit.setPlainText(self.measurement)
        self.ui.commentTextEdit.setPlainText(self.comment)
        self.ui.measurementPathLabel.setText("Path: " + self.path)

    def submit(self):
        self.accept()


    def cancel(self):
        self.reject()


    def openFolder(self):
        if sys.platform == 'darwin':
            subprocess.Popen(['open', '-R', str(self.path)])
        elif sys.platform == 'linux2':
            subprocess.Popen(['xdg-open', str(self.path)])
        elif sys.platform == 'win32':
            subprocess.Popen(['explorer', str(self.path)])
