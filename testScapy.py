from scapy.all import *
ming_ip = "172.20.63.57" #  我们要代替小明发信息
hong_ip = "172.20.72.23" #  收信人小红
ming_port = 9999 # source port (sport)
hong_port = 80 # destination port (dport)
payload = "Xiao Hong, I love you!" # packet payload 包的载荷,我们的嘿嘿嘿
spoofed_packet = IP(src=ming_ip, dst=hong_ip) / TCP(sport=ming_port, dport=hong_port) / payload
print(spoofed_packet.show())
send(spoofed_packet)