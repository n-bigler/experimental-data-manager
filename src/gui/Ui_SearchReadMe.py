# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SearchReadMe.ui'
#
# Created: Sat Sep  3 17:47:30 2016
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

class Ui_SearchReadMeDialog(object):
    def setupUi(self, SearchReadMeDialog):
        SearchReadMeDialog.setObjectName(_fromUtf8("SearchReadMeDialog"))
        SearchReadMeDialog.setWindowModality(QtCore.Qt.NonModal)
        SearchReadMeDialog.resize(533, 424)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SearchReadMeDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.titleLabel = QtGui.QLabel(SearchReadMeDialog)
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
        self.databaseURLLabel = QtGui.QLabel(SearchReadMeDialog)
        self.databaseURLLabel.setObjectName(_fromUtf8("databaseURLLabel"))
        self.horizontalLayout.addWidget(self.databaseURLLabel)
        self.rootFolderURLLineEdit = QtGui.QLineEdit(SearchReadMeDialog)
        self.rootFolderURLLineEdit.setObjectName(_fromUtf8("rootFolderURLLineEdit"))
        self.horizontalLayout.addWidget(self.rootFolderURLLineEdit)
        self.browseButton = QtGui.QPushButton(SearchReadMeDialog)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.okCancelButtonBox = QtGui.QDialogButtonBox(SearchReadMeDialog)
        self.okCancelButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.okCancelButtonBox.setCenterButtons(True)
        self.okCancelButtonBox.setObjectName(_fromUtf8("okCancelButtonBox"))
        self.horizontalLayout_2.addWidget(self.okCancelButtonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SearchReadMeDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchReadMeDialog)

    def retranslateUi(self, SearchReadMeDialog):
        SearchReadMeDialog.setWindowTitle(_translate("SearchReadMeDialog", "Form", None))
        self.titleLabel.setText(_translate("SearchReadMeDialog", "Search for new ReadMe", None))
        self.databaseURLLabel.setText(_translate("SearchReadMeDialog", "Root folder:", None))
        self.browseButton.setText(_translate("SearchReadMeDialog", "Browse...", None))

