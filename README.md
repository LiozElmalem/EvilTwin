# WiFi-EvilTwin 
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
|   '---------'       
|    _______|       
|  .'-+-+-+|         
|  '.-+-+-+|         
|    '''''' |
'-.__   __.-'

Create wifi AP that enables users to browse the internet

I'm currently working on my university projects. After that I will focus on this repo. 

## Hardware requierments
Wifi adapters - first one to monitor and second one to master.

## Report
liozelmalem7@gmail.com 

## Dependencies

* hostapd - Host AP

Default configuration: /etc/hostapd/hostapd.conf

Used to open AP wirelessly.


* dnsmasq - DHCP server + DNS server

Default configuration: /etc/dnsmasq.conf

Used to assign IP for clients on AP.

## Usage 
$ bash start.sh

## Logs 
Locate at dnsmasq area.

You can also log with dnsspoof.

Usage:
$ dnsspoof -i <name of interface of AP>
  
  
.  
