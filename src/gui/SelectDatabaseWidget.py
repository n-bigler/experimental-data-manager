# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectDatabaseWidget.ui'
#
# Created: Tue Aug 16 21:31:33 2016
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

class Ui_ParametersDialog(object):
    def setupUi(self, ParametersDialog):
        ParametersDialog.setObjectName(_fromUtf8("ParametersDialog"))
        ParametersDialog.setWindowModality(QtCore.Qt.NonModal)
        ParametersDialog.resize(533, 424)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ParametersDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.titleLabel = QtGui.QLabel(ParametersDialog)
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
        self.databaseURLLabel = QtGui.QLabel(ParametersDialog)
        self.databaseURLLabel.setObjectName(_fromUtf8("databaseURLLabel"))
        self.horizontalLayout.addWidget(self.databaseURLLabel)
        self.databaseURLLineEdit = QtGui.QLineEdit(ParametersDialog)
        self.databaseURLLineEdit.setObjectName(_fromUtf8("databaseURLLineEdit"))
        self.horizontalLayout.addWidget(self.databaseURLLineEdit)
        self.browseButton = QtGui.QPushButton(ParametersDialog)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cancelButton = QtGui.QPushButton(ParametersDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(ParametersDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ParametersDialog)
        QtCore.QMetaObject.connectSlotsByName(ParametersDialog)

    def retranslateUi(self, ParametersDialog):
        ParametersDialog.setWindowTitle(_translate("ParametersDialog", "Form", None))
        self.titleLabel.setText(_translate("ParametersDialog", "Database", None))
        self.databaseURLLabel.setText(_translate("ParametersDialog", "Database URL:", None))
        self.browseButton.setText(_translate("ParametersDialog", "Browse...", None))
        self.cancelButton.setText(_translate("ParametersDialog", "Cancel", None))
        self.okButton.setText(_translate("ParametersDialog", "Ok", None))

