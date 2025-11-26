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
sudo "^sudo" /etc/groups >> user_audit.txt # Append the list of users in the sudo group to the file
else
echo "No users found without passwords on this system"
fi