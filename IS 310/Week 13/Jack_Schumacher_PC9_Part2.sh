#!/bin/bash

## IS 310 Programming Challenge #9 Part 2
## Author: Jack Schumacher
## Contact: js0342@uah.edu

echo "Auditing user accounts"
echo "Checking if there are users without passwords"
if sudo passwd -Sa | grep -q " NP ";then
    # Print all the users in the /etc/shadow file that do not have passwords
    users_without_passwords=$(sudo awk -F: '($2 == "") {print $1}' /etc/shadow)
    printf "%s\n" "${users_without_passwords[@]}" >> user_audit.txt #Append the list of users without passwords to the file
else # If there are no users without passwords on the system
    echo "No users found without passwords on this system"
fi
sudo "^sudo" /etc/groups >> user_audit.txt # Append the list of users in the sudo group to the file

echo "Finding all writeable files"
# Find all files that are world writeable and append them into the file file_audit.txt
sudo find / -type f -perm -o+w 2>dev/null >> file_audit.txt
echo "Finding all SUID/SGID files on the system"
# These files have the permission flag /6000 and then append the results into the file_audit
sudo find / -type f -perm /6000 2>/dev/null >> file_audit.txt

echo "Checking network configurations"
sudo netstat -tulnp >> network_audit.txt #Lists all ports and their associated processes
if [ "$(sysctl -n net.ipv4.ip_forward)" -eq 1 ]; then
    echo "IPV4 forwarding is enabled"
else
    echo "IPV4 forwarding is disabled"
fi
if [ "$(sysctl -n net.ipv6.ip_forward)" ]; then
    echo "IPV6 forwarding is enabled"
else
    echo "IPV6 forwarding is disabled"
fi

# Failed login detection with line numbers using grep
echo "Looking for failed logins"
if grep -q "failed login" /var/log/auth.log;then
    grep -c "failed login" /var/log/auth.log
else
    echo "No failed login messages detected in /var/log/auth.log"
fi