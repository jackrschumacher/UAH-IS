#!/bin/bash

## IS 310 Programming Challenge #10
## Author: Jack Schumacher
## Contact: js0342@uah.edu

echo "Listing all running processes"
ps auxww # This shows all the processes in a easily readable format. Also includes processes not attached to terminal

echo "Finding all proccesses that are executing from unusual locations"
# Use wildcards to find hidden directories and inputting the most common directory locations. Will show permission denied errors if you can not access the directory
sudo ls -l /proc/*/exe | grep -E '/tmp|/dev/shm|/var/tmp|/home/.*/|.'

echo "Listing external connections and highlighting them"
# Check for all IPs that are not local
# Checks for TCP and UDP and Numeric IPs
# ss is the socket statisitics command. Only shows connections that are currently established. Uses regex to go through IPs
ss -tun state established | grep -vE "127\.|192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\."