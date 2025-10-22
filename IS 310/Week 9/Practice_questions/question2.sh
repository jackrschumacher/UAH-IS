#!/bin/bash

# Write a Bash script that checks if a given string is empty and prints a message if it is empty or not.

# Two strings that could switch if needed
empty_string=""
string=""

# -z checks if string null
if [ -z "$empty_string" ]
    then
    echo "The string is empty"
else
    echo "The string is: $string"
fi