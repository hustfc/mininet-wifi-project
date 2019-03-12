from scapy.all import sniff, sendp
from scapy.all import Packet
from scapy.all import ShortField, IntField, LongField, BitField
from scapy.all import Ether, IP, ICMP

import time

import sys
import fire

def send(src, iface, dst, times=20):
    t = 0
    alpha = 'a'
    while t < times:
        time.sleep(2)
        now = time.time()
        msg = "send_time: " + "%.6f" % float(now) + " msg: " + alpha
        print(msg)
        p = Ether() / IP(src=src, dst=dst) / ICMP() / msg
        sendp(p, iface = iface)
        t += 1
        alpha = chr(ord(alpha) + 1)
fire.Fire(send)