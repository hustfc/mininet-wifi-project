from scapy.all import sniff, sendp
from scapy.all import Packet
from scapy.all import ShortField, IntField, LongField, BitField

import sys
import struct
import time
from collections import Counter
import fire

packet_counts = Counter() 
packet_queue = []


class action:
    def __init__(self, IP, rc_pkt):
        self.ip = IP
        self.rc_pkt = rc_pkt
    def custom_action(self, packet):
        key = tuple([packet[0][1].src, packet[0][1].dst])
        if packet[0][1].dst == self.ip:
            # filename=[]
            # filename.append(packet[0][1].dst)
            # filename.append(".txt")
            filename='/home/shlled/mininet-wifi/Log/%s.txt' % packet[0][1].src[7:9]
            f=open(filename,"a+")
            packet_queue.append(packet[0][3].load)
            self.rc_pkt.append(packet[0][3].load)
            packet_counts.update([key])
            f.write('Receive Packet #%d: %s ==> %s\n' % (sum(packet_counts.values()), packet[0][1].dst, packet[0][1].src))
            print(packet.sprintf("raw : %Raw.load%"))
            now = time.time()
            #f.write("receive_time: " + "%.6f" % float(now) + "\n")
            f.close()
        sys.stdout.flush()

def receive(ip, iface, filter="icmp", rc_pkt=[]):

    sniff(iface = iface, filter= filter, timeout=10, prn = action(ip, rc_pkt).custom_action)
    

def packetQueue():
    print(packet_counts)
    print(packet_queue)

fire.Fire(receive)
#packetQueue()