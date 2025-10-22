#!/bin/bash
    
# Evaluate the status of a file or a directory

echo "Welcome to the file/directory status program"
FILE=test_file.txt

# Check if the file exists
if [ -e "$FILE" ]
    then
    # Check if the file is a directory
    if [ -f "$FILE" ]
        then
        echo "$FILE is a regular file"
    fi
    if [ -d "$FILE" ]
        then
        echo "$FILE is a directory"
    fi
    if [ -r "$FILE" ]
        then
        echo "$FILE is a readable file"
    fi
    if [ -w "$FILE" ]
        then
        echo "$FILE is writeable"
    fi
    if [ -x "$FILE" ]
        then
        echo "$FILE is executeable"
    fi

else
    echo "$FILE does not exist"
    exit 1
fi
exit
