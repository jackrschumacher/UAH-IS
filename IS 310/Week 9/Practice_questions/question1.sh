#!/bin/bash

# Write a Bash script that checks if a file named "test.txt" exists in the current directory, and if it does, prints "File exists", otherwise prints "File does not exist".
# Initialize file
FILE="test.txt"
# Check if a file exists using -e. Print the corresponding message to the shell
if [ -e "$FILE" ]
    then
    echo "The file $FILE exists"
else
    echo "The file $FILE does not exist"
fi