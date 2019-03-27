#!/usr/bin/python
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, _4address
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
# from send import send 
# from receive import receive 

import time
import thread
def command(host,arg):
    host.cmd(arg)
    thread.exit()
def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, link=wmediumd,
                       wmediumd_mode=interference, configure4addr=True)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid="ap1-ssid", mode="g",
                             channel="1", position='30,30,0')
    ap2 = net.addAccessPoint('ap2', ssid="ap2-ssid", mode="g",
                             channel="1", position='40,60,0')
    # ap3 = net.addAccessPoint('ap3', ssid="ap3-ssid", mode="g",
    #                          channel="1", position='50,30,0')
    h1 = net.addHost('h1', ip="10.0.0.1", position='30,10,0')
    h2 = net.addHost('h2', ip="10.0.0.2", position='20,20,0')
    h3 = net.addHost('h3', ip="10.0.0.3", position='30,20,0')
    h4 = net.addHost('h4', ip="10.0.0.4", position='40,20,0')
    h5 = net.addHost('h5', ip="10.0.0.5", position='50,20,0')
    h6 = net.addHost('h6', ip="10.0.0.6", position='60,20,0')
    c0 = net.addController('c0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Adding Link\n")
    net.addLink(ap1, ap2, cls=_4address) # ap1=ap, ap2=client
    #net.addLink(ap1, ap3, cls=_4address) # ap1=ap, ap3=client
    net.addLink(h1, ap1)
    net.addLink(h2, ap1)
    net.addLink(h3, ap1)
    net.addLink(h4, ap1)
    net.addLink(h5, ap1)
    net.addLink(h6, ap1)


    #net.plotGraph(max_x=100, max_y=100)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])
    #ap3.start([c0])

    try:
        thread.start_new_thread(command,(h2,"python receive.py 10.0.0.2 h2-eth0"))
        thread.start_new_thread(command,(h1,"python send.py 10.0.0.1 h1-eth0 10.0.0.2"))
        print("send finish")
    except:
        print("send error")
    
    info("*** Running CLI\n")
    CLI_wifi(net)
    
    info("*** Start sending information\n")
    # msg=[]
    # msg.append('Original')
    # print(msg)

      
    #print("start thread")
    # h2.cmd("python receive.py 10.0.0.1 h2-eth0")
    # h1.cmd("python send.py 10.0.0.1 h1-eth0 10.0.0.2")

    print("send finish")

    

    print("receive finish")
    #time.sleep(20)
    #thread.start_new_thread(command,(h2,"killall -9 python"))
    #print("kill thread")
    #h2.cmd("killall -9 receive.py")

    #receive("10.0.0.1",'h2-eth0',msg)
    #print("receive finish")

    #print(msg)


    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
