# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SyncRootFolderDialog.ui'
#
# Created: Sun Sep  4 20:29:35 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SyncRootFolderDialog(object):
    def setupUi(self, SyncRootFolderDialog):
        SyncRootFolderDialog.setObjectName(_fromUtf8("SyncRootFolderDialog"))
        SyncRootFolderDialog.setWindowModality(QtCore.Qt.NonModal)
        SyncRootFolderDialog.resize(533, 424)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SyncRootFolderDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.titleLabel = QtGui.QLabel(SyncRootFolderDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.horizontalLayout_3.addWidget(self.titleLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.databaseURLLabel = QtGui.QLabel(SyncRootFolderDialog)
        self.databaseURLLabel.setObjectName(_fromUtf8("databaseURLLabel"))
        self.horizontalLayout.addWidget(self.databaseURLLabel)
        self.rootFolderURLLineEdit = QtGui.QLineEdit(SyncRootFolderDialog)
        self.rootFolderURLLineEdit.setObjectName(_fromUtf8("rootFolderURLLineEdit"))
        self.horizontalLayout.addWidget(self.rootFolderURLLineEdit)
        self.browseButton = QtGui.QPushButton(SyncRootFolderDialog)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.okCancelButtonBox = QtGui.QDialogButtonBox(SyncRootFolderDialog)
        self.okCancelButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.okCancelButtonBox.setCenterButtons(True)
        self.okCancelButtonBox.setObjectName(_fromUtf8("okCancelButtonBox"))
        self.horizontalLayout_2.addWidget(self.okCancelButtonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SyncRootFolderDialog)
        QtCore.QMetaObject.connectSlotsByName(SyncRootFolderDialog)

    def retranslateUi(self, SyncRootFolderDialog):
        SyncRootFolderDialog.setWindowTitle(_translate("SyncRootFolderDialog", "Form", None))
        self.titleLabel.setText(_translate("SyncRootFolderDialog", "Search for new ReadMe", None))
        self.databaseURLLabel.setText(_translate("SyncRootFolderDialog", "Root folder:", None))
        self.browseButton.setText(_translate("SyncRootFolderDialog", "Browse...", None))

