#!/bin/bash

# Check if a file exists based upon a command line argument

# Take input from 
if [ $# -ne 1 ]
then
    echo "Usage - $0 file-name"
    exit 1
fi
# Checking if the file exists
if [ -f "$1" ]
then
echo "This file exists"
cat "$1"
else
echo "This file does not exist"
fi