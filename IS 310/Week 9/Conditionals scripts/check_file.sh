#!/bin/bash

# Check if the file exists
FILE="./test_file.sh"

if [ -e "$FILE" ]
    then
    if [ -x "$FILE" ]
        then
        $FILE
    else
        echo "This script is not executeable"
    fi
else
    echo "The File $FILE is not reachable"
fi
