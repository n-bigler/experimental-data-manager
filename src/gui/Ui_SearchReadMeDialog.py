# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SearchReadMeDialog.ui'
#
# Created: Tue Sep  6 20:23:51 2016
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

class Ui_Ui_SearchReadMeDialog(object):
    def setupUi(self, Ui_SearchReadMeDialog):
        Ui_SearchReadMeDialog.setObjectName(_fromUtf8("Ui_SearchReadMeDialog"))
        Ui_SearchReadMeDialog.setWindowModality(QtCore.Qt.NonModal)
        Ui_SearchReadMeDialog.resize(566, 420)
        self.verticalLayoutWidget = QtGui.QWidget(Ui_SearchReadMeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 561, 421))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(15)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 557, 356))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Ui_SearchReadMeDialog)
        QtCore.QMetaObject.connectSlotsByName(Ui_SearchReadMeDialog)

    def retranslateUi(self, Ui_SearchReadMeDialog):
        Ui_SearchReadMeDialog.setWindowTitle(_translate("Ui_SearchReadMeDialog", "Dialog", None))
        self.label.setText(_translate("Ui_SearchReadMeDialog", "Searching for readme...", None))

