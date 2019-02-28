import sys

from mininet.log import setLogLevel, info
from mininet.node import Controller
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
from time import sleep

def topology(D2D, AP):
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', wlans=2, position='5,5,0',
                          mac='00:00:00:00:00:01', ip='10.0.0.1/8')
    sta2 = net.addStation('sta2', wlans=2, position='15,5,0',
                          mac='00:00:00:00:00:02', ip='10.0.0.2/8')
    if AP:
        ap1 = net.addAccessPoint('ap1', ssid='ssid-ap1', mode='g', channel='1',
                             position='10,10,0')
    c1 = net.addController('c1')

    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    net.plotGraph(max_x=20, max_y=20)

    sta1.cmd('iw dev %s interface add mon0 type monitor' % sta1.params['wlan'][0])
    sta1.cmd('ifconfig mon0 up')
    sta1.cmd('wireshark -i mon0 &')

    info("*** Creating links\n")
    if AP:
        net.addLink(ap1, sta1)
        net.addLink(ap1, sta2)
    if D2D:
        net.addLink(sta1, cls=adhoc, ssid='adhocNet',
                    mode='g', channel=5, ht_cap='HT40+')
        net.addLink(sta2, cls=adhoc, ssid='adhocNet',
                    mode='g', channel=5)

    info("*** Starting network\n")
    net.build()
    c1.start()
    if AP:
        ap1.start([c1])

    info("*** Print network status messages\n")
    info("\nsta1 status:\n")
    info('%s\n' % sta1.cmd('iwconfig'))
    info("sta2 status:\n")
    info('%s\n' % sta2.cmd('iwconfig'))

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    D2D = True if '-d' in sys.argv else False
    AP = True if '-a' in sys.argv else False
    topology(D2D, AP)