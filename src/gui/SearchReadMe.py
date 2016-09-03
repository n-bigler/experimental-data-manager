"""TODO: Write doc
"""

import sys
from PyQt4 import QtGui, QtCore
from src.gui import Ui_SearchReadMe

class SearchReadMe(QtGui.QDialog):
    def __init__(self, parent=None, currentPath='.'):
        super(self.__class__, self).__init__()
        QtGui.QDialog.__init__(self, parent)

        self.ui = Ui_SearchReadMe.Ui_SearchReadMeDialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.browseButton.released.connect(self.browse)
        self.currentPath = currentPath;
        # first initialize line edit with current path
        self.ui.rootFolderURLLineEdit.setText(currentPath)
        # then setup a slot for any edit of line edit
        self.ui.rootFolderURLLineEdit.textChanged.connect(self.urlChanged)

        #ok and cancel buttons
        self.ui.okCancelButtonBox.accepted.connect(self.submit)
        self.ui.okCancelButtonBox.rejected.connect(self.cancel)


    def urlChanged(self, newURL):
        self.currentPath = newURL


    def browse(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, True)
        dialog.setDirectory(self.ui.databaseURLLineEdit.displayText())
        if dialog.exec_():
            files = dialog.selectedFile()
            self.ui.rootFolderURLLineEdit.setText(files.first())


    def getValues(self):
        return self.currentPath

    def submit(self):
        self.accept()

    def cancel(self):
        self.reject()
