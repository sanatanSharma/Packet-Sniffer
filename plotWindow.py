# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotWindow.ui'
#
# Created: Wed Mar  9 22:13:04 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import netifaces

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

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(441, 286)
        self.centralwidget = QtGui.QWidget(plotWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(200, 90, 121, 31))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 150, 121, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 50, 161, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        plotWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(plotWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        plotWindow.setStatusBar(self.statusbar)

        self.retranslateUi(plotWindow)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(_translate("plotWindow", "MainWindow", None))
        self.label.setText(_translate("plotWindow", "Enter Date:", None))
        self.pushButton.setText(_translate("plotWindow", "Show Plot", None))
        self.label_2.setText(_translate("plotWindow", "Choose Your Interface:", None))

    def setOptions(self):
        l = netifaces.interfaces()
        for i in range(0,len(l)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(i, _translate("Sniffer", l[i], None))

