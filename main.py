from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4.QtCore import *
from netifaces import AF_INET
import time
import sys 
from requests import get# We need sys so that we can pass argv to QApplication

import mainWindow
import sniffWindow
import sniffPacket 
import statsWindow
import showDatabaseWindow

import netifaces # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer           # It sets up layout and widgets that are defined

class Win1(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setOptions()
        # self.public_ip = get('https://api.ipify.org').text
        self.public_ip = "dbcbh"
        self.pushButton.clicked.connect(self.handleButton)
        self.actionStatistics.triggered.connect(self.handleActionStats)
        self.window2 = None
        self.window3 = None
        
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

class Win2(QtGui.QMainWindow, sniffWindow.Ui_sniffWindow):

    def __init__(self, IP, text, public_ip):
        QtGui.QMainWindow.__init__(self)
        self.txt = text 
        self.Ip = IP
        self.public_ip = public_ip
        self.thread = sniffPacket.sniffThread()
        self.setupUi(self, self.Ip, self.txt, self.public_ip)
        # self.connect(self.thread, SIGNAL("finished()"), self.updateUi)
        # self.connect(self.thread, SIGNAL("terminated()"), self.updateUi)

        self.connect(self.thread, SIGNAL("output(PyQt_PyObject)"), self.printScreen)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.handleButton)
        
        # self.pushButton.clicked.connect(self.handleButton)

    def handleButton(self):
        self.thread.render(self.Ip, self.txt)

    def printScreen(self,l):
        self.pushEntry(l)

    

class Win3(QtGui.QMainWindow, statsWindow.Ui_statsWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handleButton)
        self.window2 = None

    def handleButton(self):
        temp = self.dateEdit.date()
        date = temp.toPyDate() 
        print date
        if self.window2 is None:
            self.window2 = Win4()
        self.window2.show()
        self.window2.showPackets(date)


class Win4(QtGui.QMainWindow, showDatabaseWindow.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)



def main():
    app = QtGui.QApplication(sys.argv)
    window = Win1()
    window.show()                         
    sys.exit(app.exec_())                 


if __name__ == '__main__':              
    main()  

