from PyQt4 import QtGui 
from PyQt4.QtCore import *
from netifaces import AF_INET
from requests import get

import time
import sys 


import mainWindow
import sniffWindow
import sniffPacket 
import databaseWindow
import showDatabaseWindow
import plotWindow
import databaseM
import plot

import netifaces 

class Win1(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setOptions()
        # self.public_ip = get('https://api.ipify.org').text
        self.public_ip = "dc"
        self.pushButton.clicked.connect(self.handleButton)
        self.actionStatistics.triggered.connect(self.handleActionStats)
        self.actionPlot.triggered.connect(self.handleActionPlot)
        self.window2 = None
        self.window3 = None
        self.window4 = None
        
    def handleButton(self):
        txt = self.comboBox.currentText()
        Ip = netifaces.ifaddresses(str(txt))[AF_INET][0]['addr']
        if self.window2 is None:
            self.window2 = Win2(Ip, txt, self.public_ip)
        self.window2.show()

    def handleActionStats(self):
        if self.window3 is None:
            self.window3 = Win3()
        self.window3.show()

    def handleActionPlot(self):
        if self.window4 is None:
            self.window4 = Win5()
        self.window4.show()

class Win2(QtGui.QMainWindow, sniffWindow.Ui_sniffWindow):

    def __init__(self, IP, text, public_ip):
        QtGui.QMainWindow.__init__(self)
        self.txt = text 
        self.Ip = IP
        self.public_ip = public_ip
        self.thread = sniffPacket.sniffThread()
        self.setupUi(self, self.Ip, self.txt, self.public_ip)

        self.connect(self.thread, SIGNAL("output(PyQt_PyObject)"), self.printScreen)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.handleButton)
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.handleTermination)

    def handleButton(self):
        self.thread.render(self.Ip, self.txt)

    def printScreen(self,l):
        self.pushEntry(l)

    def handleTermination(self):
        self.thread.stop()

    

class Win3(QtGui.QMainWindow, databaseWindow.Ui_databaseWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setOptions()
        self.pushButton.clicked.connect(self.handleButton)
        self.window2 = None

    def handleButton(self):
        interface = self.comboBox.currentText()
        temp = self.dateEdit.date()
        date = temp.toPyDate() 
        print date
        if self.window2 is None:
            self.window2 = Win4()
        self.window2.show()
        self.window2.showPackets(date, interface)


class Win4(QtGui.QMainWindow, showDatabaseWindow.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)


class Win5(QtGui.QMainWindow, plotWindow.Ui_plotWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setOptions()
        self.pushButton.clicked.connect(self.handleButton)
        self.window2 = None

    def handleButton(self):
        interface = self.comboBox.currentText()
        temp = self.dateEdit.date()
        date = temp.toPyDate()
        plot.connectDatabase2(date, interface)

def main():
    app = QtGui.QApplication(sys.argv)
    window = Win1()
    window.show()                         
    sys.exit(app.exec_())                 


if __name__ == '__main__':              
    main()  

