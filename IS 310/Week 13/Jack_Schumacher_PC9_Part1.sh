#!/bin/bash

## IS 310 Programming Challenge #9 Part 1
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Disabling Unnecessary Services- telnet, ftp, and rsh
#Stop the telnet service using systemd- also prevent from starting at startup and having other system processes start it
# Check if the telnet service is enabled on the system, if not print a error
echo "Checking if the telnet service is enabled"
if systemctl list-unit-files | grep -q "telnet";then
    sudo systemctl status telnet.socket
    echo "Disabling telnet services"
    sudo systemctl stop telnet.socket
    sudo systemctl disable telnet.socket
    sudo systemctl mask telnet.socket
else
    echo "The telnet service is not enabled on this system"
fi

# Disabling ftp
if systemctl list-unit-files | grep -q "vsftpd";then
    sudo systemctl stop vsftpd
else
    echo "The ftp service is not enabled on this system"
fi

# Disabling rsh- also stop on boot
if systemctl list-unit-files | grep -q "rsh";then
    sudo systemctl stop rsh.socket rsh.service
    sudo systemctl disable rsh.socket rsh.service
else
    echo "The rsh service is not enabled on this system"
fi

# Configure firewall rules
# Block all incoming traffic by default. Allow SSH on port 22. Allow HTTP on port 80. Make sure all users on the system have a password
echo "Configuring the firewall"
sudo ufw default deny incoming # Deny all incoming traffic
sudo ufw allow ssh #Allow only port 22 on ssh - this is the standard behavior
sudo ufw allow 80/tcp #Allow http on port 80
sudo ufw enable #Enable firewall

# Expiring passwords and locking accounts
echo "Expiring the root user password"
sudo passwd -e root
if id "guest" &>/dev/null; then
    sudo usermod -L guest # Lock the guest account
    sudo usermod -s /sbin/nologin guest #Lock the guest's shell access
else
    echo "The guest user could not be found on this system" #Prints if the guest user does not exist
fi

echo "Checking if there are users with password"
if sudo passwd -Sa | grep -q " NP ";then
    echo "Found users with no passwords. Removing them now"
    users_without_passwords=$(sudo awk -F: '($2 == "") {print $1}' /etc/shadow) # Create a list of all the users without passwords in order to cycle through them and remove thier permissions (parsing using the second field)
    # For the users without passwords, lock them and remove thier shell access as well
    for users in $users_without_passwords; do
        sudo passwd -l "$users"
        sudo usermod -s /sbin/nologin "$users"
        echo "The user: $users has been locked"
    done
else
    echo "All users have passwords"
fi

echo "Performing system update"
sudo do-release-upgrade # This command works with all major operating systems
sudo apt update
echo "Updating the following packages:"
apt list --upgradeable
sudo apt upgrade -y #Using the -y flag to allow all prompts
echo "Removing unused packages"
sudo apt autoremove #Autoremove unused packages
