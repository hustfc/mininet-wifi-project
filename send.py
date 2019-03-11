from scapy.all import sniff, sendp
from scapy.all import Packet
from scapy.all import ShortField, IntField, LongField, BitField
from scapy.all import Ether, IP, ICMP

import time

import sys

def send(src, dst, times=20):
    t = 0
    while t < times:
        time.sleep(4)
        now = time.time()
        msg = "send_time: " + "%.6f" % float(now) + " msg: "
        print(msg)
        #msg = str(now) + " " + raw
        p = Ether() / IP(src=src, dst=dst) / ICMP() / msg
        sendp(p, iface = "sta1-wlan0")
        # print msg
        t += 1
send('10.0.0.1','10.0.0.2')