# Stop the deamons

pkill -9 hostapd &
pkill -9 dnsmasq &
pkill -9 apache2 &

# Rewrite the original resolv.conf

service network-manager restart
rm /etc/resolv.conf
echo nameserver 8.8.8.8 > /etc/resolv.conf