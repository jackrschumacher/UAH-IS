#!/bin/bash

## IS 310 Programming Challenge #8 Part 3
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Declare arrays used in this project
declare -a error_Messages
declare -a critical_Messages
declare -a IP_Adresses_Unflitered
declare -a IP_Adresses_Filtered

# Define variables for file names to allow for global changes easily
formatted_errors=formatted_critical_errors.log
critical_error_log=critical_errors.log

read -p "Please enter a filename to search: " filename
# Check if the file exists
if [ -f "$filename" ];then
    # Grep for "critical" amd "critical" messages in the file and assign to arrays in order to more easily put in other files
    echo "File load for $filename was successful"
    mapfile -t error_Messages < <(grep "error" "$filename")
    mapfile -t critical_Messages < <(grep "critical" "$filename")
    # Print the "error" and "critical" arrays into the critical_errors.log
    echo "Error messages:" > critical_errors.log
    printf "%s\n" "${error_Messages[@]}" >> $critical_error_log
    printf "%s\n" "${critical_Messages[@]}" >> $critical_error_log
    # Replace capitalized messages with lowercase messages
    sed  's/ERROR/error/p; s/CRITICAL ALERT/critical/gp' $critical_error_log  > $formatted_errors
    # Print and sort timestamps from the formatted_errors
    echo "Timestamps from $formatted_errors"
    grep -E "\d{4}-\d{2}-\d{2} T\d{2}:\d{2}:\d{2} " $formatted_errors | sort

    mapfile -t IP_Adresses_Unflitered < <(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' $filename) # Use regex in order to find all IP adresses and save to an unfiltered array\
    mapfile -t IP_Adresses_Filtered < <(printf "%s\n" "${IP_Adresses_Unflitered[@]}" | sort -u) #Only write unique IP values into the filtered array
    unique_Adresses=${#IP_Adresses_Filtered[@]} #Count the number of items in the unique array (using the # symbol)
    echo "Unique IP adresses count: $unique_Adresses" # Print the number of unique items in the array
    # Print the first 10 occurances of the word "failed" in the formatted errors file.
    echo "First 10 occurances of failed:"
    grep -m 10 "failed" $formatted_errors
else
    echo "File load for $filename unsuccessful"
fi