#!/bin/bash

## IS 310 Programming Challenge #8 Part 2
## Author: Jack Schumacher
## Contact: js0342@uah.edu

echo "Programming Challenge 8 Part 2"

# Have the user enter a log file to search through
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

echo "Authentication failure message"
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
if [ -f $filename ];then
    # Count the number of occurances of each of the messages (error, warning, info)
    error_Count=$(grep -c "error" $filename)
    warning_Count=$(grep -c "warning" $filename)
    info_Count=$(grep -c "info" $filename)
    file_Length=$(wc -l < "$filename")
    # Print the number of errors, warnings and info messages to the console
    echo "Number of errors found in $filename: $error_Count"
    echo "Number of warnings found in $filename: $warning_Count"
    echo "Number of info messages found in $filename: $info_Count"
    # The echo -e command allows to write multiple lines to one file (using \n)
    echo -e "Security report \n File Length: $file_Length lines \n Error message count: $error_Count \n Warning message count: $warning_Count" >> Security_Report.txt
else
    echo "File load unsucessful"
fi



