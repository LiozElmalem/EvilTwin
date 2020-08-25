# **Wifi Evil Twin**

![](https://designcontest-com-au-designcontest.netdna-ssl.com/data/contests/302364/entries/2daaf5f30aefca34.png)

### Required

- 2 Wifi adapters - first one to monitor and second one to master.
- Ethernet connection
- Linux system 
- Services:
	- apache2 - Web server.
	- hostapd - Host AP Default configuration: /etc/hostapd/hostapd.conf Used to open AP wirelessly.
	- dnsmasq - DHCP server + DNS server Default configuration: /etc/dnsmasq.conf Used to assign IP for clients on AP.

### Setup environment

- Terminal command

    `$ ./setup.sh`

### Usage

- Start command

    `$ python console.py`

- Reset command

    `$ ./reset.sh`

----

### Credits
- Wikipedia - https://en.wikipedia.org/wiki/Evil_twin_(wireless_networks)
- Airgeddon - https://github.com/v1s1t0r1sh3r3/airgeddon
- Wirespy - https://github.com/aress31/wirespy
- Gabriel Ryan - https://github.com/s0lst1c3/evil_twin
