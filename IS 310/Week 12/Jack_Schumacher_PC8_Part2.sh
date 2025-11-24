#!/bin/bash

## IS 310 Programming Challenge #8 Part 2
## Author: Jack Schumacher
## Contact: js0342@uah.edu

echo "Programming Challenge 8 Part 2"

# Locate the log files found in the log folder that have the ".log" suffix
echo "Locating system log files"
sudo find /var/log -name "*log"

echo "Security vulnerability check"
read -p "Please enter a filename to search for security vulnerabilities: " filename

# Checking if the file provided exists, if not printing an error message and exiting the program
if [[ -f "$filename" ]]; then
    echo "File load for $filename successful"
    if grep -q "Speculative Store Bypass is enabled" "$filename";then
        echo "This system is vulnerable to Speculative Store Bypass"
    elif grep -q "Speculative Store Bypass is disabled" "$filename";then
        echo "This system is not vulnerable to Speculative Store Bypass"
    else
        echo "Could not determine if this system is vulnerable to Speculative Store Bypass"
    fi
else
    echo "File load operation for $filename was unsuccessful" >&2
    exit 1
fi
# Authentication failure detection with line numbers using grep
echo "Authentication failure detection"
echo "authentication failure message"
if grep -q "authentication failure" $filename;then
    grep -qn "authentication failure" $filename
else
    echo "No authentication messages detected in $filename"
fi
# Failed login detection with line numbers using grep
echo "Failed login detection"
if grep -q "failed login" $filename;then
    grep -qn "failed login" $filename
else
    echo "No failed login messages detected in $filename"
fi

echo "Log severity count"




