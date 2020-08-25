# **Wifi Evil Twin**

![](https://designcontest-com-au-designcontest.netdna-ssl.com/data/contests/302364/entries/2daaf5f30aefca34.png)

### Required

- 2 Wifi adapters - first one to monitor and second one to master.
- Ethernet connection
- Linux system 
- Services:
	- apache2  
	- hostapd - Host AP Default configuration: /etc/hostapd/hostapd.conf Used to open AP wirelessly.
	- dnsmasq - DHCP server + DNS server Default configuration: /etc/dnsmasq.conf Used to assign IP for clients on AP.

###Links

[Links](http://localhost/)

[Links with title](http://localhost/ "link title")

`<link>` : <https://github.com>

[Reference link][id/name] 

[id/name]: http://link-url/

GFM a-tail link @pandao

### Setup environment

#### terminal command

`$ ./setup.sh`

### Usage

#### start command

`$ python console.py`

#### reset command

`$ ./reset,sh`

----

###FlowChart

```flow
st=>start: Login
op=>operation: Login operation
cond=>condition: Successful Yes or No?
e=>end: To admin

st->op->cond
cond(yes)->e
cond(no)->op
```

###Sequence Diagram
                    
```seq
Andrew->China: Says Hello 
Note right of China: China thinks\nabout it 
China-->Andrew: How are you? 
Andrew->>China: I am good thanks!
```

###End
