
# Reset to start.sh executes
systemctl enable systemd-resolved.service 
systemctl start systemd-resolved
service network-manager restart

# Bad resolv.conf configure , i just need to reset for each iteration
rm /etc/resolv.conf
echo nameserver 8.8.8.8 > /etc/resolv.conf
