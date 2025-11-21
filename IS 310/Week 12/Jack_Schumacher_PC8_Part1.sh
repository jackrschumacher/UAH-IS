#!/bin/bash

## IS 310 Programming Challenge #8
## Author: Jack Schumacher
## Contact: js0342@uah.edu

declare -a IP_Adresses

echo "Programming Challenge 8"
read -p "Please enter a filename: " filename
# Check if the file name exists if yes print success mesage, if not exit and print an error message
if [[ -f "$filename" ]]; then
    echo "File load for $filename successful"   
    # Check if the word "administrator" occurs in the file
    if grep -q "administrator" $filename;then
        echo "Match found. Please check all security logs"
    else
        echo "Match not found: Please proceed with system update"
    fi
    echo "Finding logons"
    grep "Logon ID" $filename
    # Show the changes before making them
    echo "Account matches"
    sed -n 's/Account/Local/gp' $filename 
    echo "Administrator matches"
    sed -n 's/administrator/local_user/gp' $filename
    sed -i 's/Account/Local/g' $filename #g flag ensures replacements occur even if there are multiple matches on the same line
    sed -i 's/administrator/local_user/g' $filename
    printf "Security ID occurances: "
    grep -o "Security ID" $filename | wc -l #Combine the grep and word count utilities to count the number of occurances of a word
    echo "Timestamp sorting"
    grep "Timestamp" $filename | sort 
    # Use regex to filter the file and save to array
    mapfile -t IP_Adresses < <(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' $filename)
    echo IP_Adresses >> IP_Adresses.txt
    echo "Saved IP Adresses!"
    exit 0

else
    echo "File load for $filename unsucessful" >&2 #Redirect the error message into the exit message
    exit 1
fi
