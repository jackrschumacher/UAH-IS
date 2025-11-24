#!/bin/bash

## IS 310 Programming Challenge #8 Part 3
## Author: Jack Schumacher
## Contact: js0342@uah.edu

declare -a error_Messages
declare -a critical_Messages
declare -a IP_Adresses
formatted_errors=formatted_critical_errors.log
critical_error_log=critical_errors.log
read -p "Please enter a filename to search: " filename
if [ -f "$filename" ];then
echo "File load for $filename was successful"
mapfile -t error_Messages < <(grep "error" "$filename")
mapfile -t critical_Messages < <(grep "critical" "$filename")
echo "Error messages:" > critical_errors.log
printf "%s\n" "${error_Messages[@]}" >> $critical_error_log
printf "%s\n" "${critical_Messages[@]}" >> $critical_error_log
sed  's/ERROR/error/p; s/CRITICAL ALERT/critical/gp' $critical_error_log  > $formatted_errors
echo "Timestamps from $formatted_errors"
grep -E "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}" $formatted_errors | sort

else
echo "File load for $filename unsuccessful"
fi