# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sniffWindow.ui'
#
# Created: Fri Mar  4 11:13:29 2016
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

class Ui_sniffWindow(object):
    def setupUi(self, sniffWindow, ip, txt, public_ip):
        sniffWindow.setObjectName(_fromUtf8("sniffWindow"))
        sniffWindow.resize(586, 489)
        self.centralwidget = QtGui.QWidget(sniffWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        sniffWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(sniffWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        sniffWindow.setStatusBar(self.statusbar)

        self.retranslateUi(sniffWindow, ip, txt, public_ip)
        QtCore.QMetaObject.connectSlotsByName(sniffWindow)

    def retranslateUi(self, sniffWindow, ip, txt, public_ip):
        sniffWindow.setWindowTitle(_translate("sniffWindow", "MainWindow", None))
        self.label_4.setText(_translate("sniffWindow", public_ip, None))
        self.label_6.setText(_translate("sniffWindow", txt, None))
        self.label_2.setText(_translate("sniffWindow", "Local IP", None))
        self.label_3.setText(_translate("sniffWindow", "Interface", None))
        self.label_5.setText(_translate("sniffWindow", ip , None))
        self.label.setText(_translate("sniffWindow", "Public IP", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("sniffWindow", "Source IP", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("sniffWindow", "Destination IP", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("sniffWindow", "TCP Source Port", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("sniffWindow", "TCP Dest. Port", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("sniffWindow", "Start Sniffin'!", None))



    def pushEntry(self, l):
        rows = self.tableWidget.rowCount()
        rows = rows+1
        self.tableWidget.setRowCount(rows)
        rows = rows-1
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(rows, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(rows, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(rows, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(rows, 3, item)
        item = self.tableWidget.item(rows, 0)
        item.setText(_translate("sniffWindow", l[0] , None))
        item = self.tableWidget.item(rows, 1)
        item.setText(_translate("sniffWindow", l[1] , None))
        item = self.tableWidget.item(rows, 2)
        item.setText(_translate("sniffWindow", l[2] , None))
        item = self.tableWidget.item(rows, 3)
        item.setText(_translate("sniffWindow", l[3] , None))

