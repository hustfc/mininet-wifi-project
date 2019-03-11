from scapy.all import sniff, sendp
from scapy.all import Packet
from scapy.all import ShortField, IntField, LongField, BitField

import sys
import struct
import time
from collections import Counter

packet_counts = Counter()
packet_queue = []

def custom_action(packet):
    key = tuple([packet[0][1].src, packet[0][1].dst])
    if packet[0][1].dst == '10.0.0.2':
        packet_queue.append(packet[0][3].load)
        packet_counts.update([key])
        print('Receive Packet #%d: %s ==> %s' % (sum(packet_counts.values()), packet[0][1].src, packet[0][1].dst))
        print(packet.sprintf("raw : %Raw.load%"))
        now = time.time()
        print("receive_time: " + "%.6f" % float(now) + "\n")
    sys.stdout.flush()

def receive(iface, filter):
    sniff(iface = iface, filter= filter, prn = custom_action)

def packetQueue():
    print(packet_counts)
    print(packet_queue)
    #print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: {count}" for key, count in packet_counts.items()))

iface = "sta2-wlan0"
filter = "icmp"

receive(iface, filter)
packetQueue()