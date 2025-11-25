#!/bin/bash

## IS 310 Programming Challenge #9
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Disabling Unnecessary Services- telenet, ftp, and rsh
#Stop the telenet service using systemd- also prevent from starting at startup and having other system processes start it
echo "Disabling telenet services"
sudo systemctl stop telenet.socket
sudo systemctl disable telenet.socket
sudo systemctl mask telenet.socket

# Disabling ftp
sudo systemctl stop vsftpd

# Disabling rsh- also stop on boot
sudo systemctl stop rsh.socket rsh.service
sudo systemctl disable rsh.socket rsh.service

# Configure firewall rules
# Block all incoming traffic by default. Allow SSH on port 22. Allow HTTP on port 80. Make sure all users on the system have a password
sudo ufw default deny incoming # Deny all incoming traffic
sudo ufw allow ssh #Allow only port 22 on ssh - this is the standard behavior
sudo ufw allow 80/tcp #Allow http on port 80
sudo ufw enable #Enable firewall

