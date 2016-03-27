from scapy.all import *
import sniffWindow
from PyQt4.QtCore import *
import databaseM

class sniffThread(QThread):

    interface = "" 
    hostIP = "host "
    
    def render(self, IP, intF):
        self.interface += str(intF)
        self.hostIP += str(IP)
        self.start()

    def run(self):
        print "\nScanning..."
        print "Source IP          Destination IP        Source Port       Destination Port"
        sniff(filter=self.hostIP,prn=self.print_summary,iface=self.interface)

    def print_summary(self,pkt):
        # info = []
        if IP in pkt:
            ip_src=pkt[IP].src
            ip_dst=pkt[IP].dst
            
        if TCP in pkt:
            tcp_sport=pkt[TCP].sport
            tcp_dport=pkt[TCP].dport

            l = [str(ip_src),str(ip_dst),str(tcp_sport),str(tcp_dport), str(self.interface)]
            self.storeInDatabase(l)
            self.emit(SIGNAL("output(PyQt_PyObject)"),l)

    def storeInDatabase(self,l):
        databaseM.addToTable(l)

    def stop(self):
        self.terminate()


    