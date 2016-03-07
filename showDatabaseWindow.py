# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showDatabase.ui'
#
# Created: Tue Mar  8 00:52:39 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(586, 489)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def showPackets(self, date):
        db = MySQLdb.connect("localhost","root","1234","log")
        cursor = db.cursor()
        sql = "SELECT * FROM packets WHERE `Date`='%s'" % (date)
        cursor.execute(sql)

        for row in cursor:
            l = [str(row[1]),str(row[2]),str(row[3]),str(row[4])]
            self.pushEntry(l)
        db.commit()
        db.close()



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Source IP", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source Ip", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TCP Source Port", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TCP Dest. Port", None))

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
        item.setText(_translate("MainWindow", l[0] , None))
        item = self.tableWidget.item(rows, 1)
        item.setText(_translate("MainWindow", l[1] , None))
        item = self.tableWidget.item(rows, 2)
        item.setText(_translate("MainWindow", l[2] , None))
        item = self.tableWidget.item(rows, 3)
        item.setText(_translate("MainWindow", l[3] , None))

