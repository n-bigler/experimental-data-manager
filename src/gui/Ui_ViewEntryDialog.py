# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ViewEntryDialog.ui'
#
# Created: Sun Aug 28 18:26:01 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(607, 642)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 551, 611))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.measurementPathLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.measurementPathLabel.setObjectName(_fromUtf8("measurementPathLabel"))
        self.verticalLayout.addWidget(self.measurementPathLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.projectLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectLineEdit.sizePolicy().hasHeightForWidth())
        self.projectLineEdit.setSizePolicy(sizePolicy)
        self.projectLineEdit.setObjectName(_fromUtf8("projectLineEdit"))
        self.horizontalLayout.addWidget(self.projectLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateLineEdit.sizePolicy().hasHeightForWidth())
        self.dateLineEdit.setSizePolicy(sizePolicy)
        self.dateLineEdit.setObjectName(_fromUtf8("dateLineEdit"))
        self.horizontalLayout_2.addWidget(self.dateLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.measurementTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurementTextEdit.sizePolicy().hasHeightForWidth())
        self.measurementTextEdit.setSizePolicy(sizePolicy)
        self.measurementTextEdit.setObjectName(_fromUtf8("measurementTextEdit"))
        self.verticalLayout.addWidget(self.measurementTextEdit)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.commentTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commentTextEdit.sizePolicy().hasHeightForWidth())
        self.commentTextEdit.setSizePolicy(sizePolicy)
        self.commentTextEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.commentTextEdit.setObjectName(_fromUtf8("commentTextEdit"))
        self.verticalLayout.addWidget(self.commentTextEdit)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Discard|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "Edit entry", None))
        self.measurementPathLabel.setText(_translate("Dialog", "Path:", None))
        self.label.setText(_translate("Dialog", "Project", None))
        self.label_2.setText(_translate("Dialog", "Date", None))
        self.label_3.setText(_translate("Dialog", "Measurement", None))
        self.label_4.setText(_translate("Dialog", "Comment", None))

