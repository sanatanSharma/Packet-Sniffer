from scapy.all import *
import sniffWindow
from PyQt4.QtCore import *

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

            l = [str(ip_src),str(ip_dst),str(tcp_sport),str(tcp_dport)]
            # s = str(ip_src) + "   ->   " + str(ip_dst) + "        " + str(tcp_sport) + "                  "+ str(tcp_dport)
            self.emit(SIGNAL("output(PyQt_PyObject)"),l)
            # sniffWindow.pushEntry(str(ip_src),str(ip_dst))
            # print str(ip_src) + "   ->   " + str(ip_dst) + "        " + str(tcp_sport) + "                  "+ str(tcp_dport)
        # print "sd"
        # http_packet = str(pkt)
        # if http_packet.find(" "):
        # 	f = open('log.txt',"a")
        #     f.write(str(GET_print(pkt)))
        
    # def GET_print(packet1):
    #     ret = "***************************************GET PACKET****************************************************\n"
    #     ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    #     ret += "*****************************************************************************************************\n"
    #     return ret

        # hexdump(pkt)
    # info = []

    