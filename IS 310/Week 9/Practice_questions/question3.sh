#!/bin/bash

#Write a Bash script that checks if a given number is even or odd and prints a message if it is even or if it is odd.
echo "Even or odd number?"
printf "Please enter a number:"
read entered_number

# Mod entered number to determine if even and odd
if ((entered_number % 2 == 0))
    then
    echo "The number $entered_number is even."
else
    echo "The number $entered_number is odd."
fi
