# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Feb 25 16:52:14 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
import netifaces
# import sniffWindow

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


class Ui_Sniffer(object):
    def setupUi(self, Sniffer):
        Sniffer.setObjectName(_fromUtf8("Sniffer"))
        Sniffer.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Sniffer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 140, 160, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 250, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Sniffer.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Sniffer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Sniffer.setStatusBar(self.statusbar)

        self.retranslateUi(Sniffer)
        QtCore.QMetaObject.connectSlotsByName(Sniffer)

    def retranslateUi(self, Sniffer):
        Sniffer.setWindowTitle(_translate("Sniffer", "Sniffer", None))
        self.label.setText(_translate("Sniffer", "Choose Your Interface", None))
        self.pushButton.setText(_translate("Sniffer", "Start", None))


    def setOptions(self):
        l = netifaces.interfaces()
        for i in range(0,len(l)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(i, _translate("Sniffer", l[i], None))


