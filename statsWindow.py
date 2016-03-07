# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statsWindow.ui'
#
# Created: Mon Mar  7 23:04:06 2016
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

class Ui_statsWindow(object):
    def setupUi(self, statsWindow):
        statsWindow.setObjectName(_fromUtf8("statsWindow"))
        statsWindow.resize(441, 286)
        self.centralwidget = QtGui.QWidget(statsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(200, 90, 111, 31))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 170, 121, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 170, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        statsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(statsWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        statsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(statsWindow)
        QtCore.QMetaObject.connectSlotsByName(statsWindow)

    def retranslateUi(self, statsWindow):
        statsWindow.setWindowTitle(_translate("statsWindow", "Statistics", None))
        self.label.setText(_translate("statsWindow", "Enter Date:", None))
        self.pushButton.setText(_translate("statsWindow", "Show Database", None))
        self.pushButton_2.setText(_translate("statsWindow", "Plot", None))

