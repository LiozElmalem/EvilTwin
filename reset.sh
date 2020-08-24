rm /etc/resolv.conf
echo nameserver 8.8.8.8 > /etc/resolv.conf

systemctl enable systemd-resolved.service 
systemctl start systemd-resolved
service network-manager restart
