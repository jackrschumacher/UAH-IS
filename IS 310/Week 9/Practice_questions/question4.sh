#!/bin/bash

# Write a Bash script that prompts the user to enter a number and checks if it is positive,negative, or zero, and prints a message accordingly.
echo "Number checker"
echo "This program checks if a number is positive, negative or zero"
printf "Please enter a number"
read entered_number

# Check if the value that is entered is an integer value
if [[ "$entered_number" =~ ^[+-]?[0-9]+$ ]]; then
    if ((entered_number > 0)); then
        echo "$entered_number is positive"
    elif ((entered_number < 0)); then
        echo "$entered_number is negative"
    elif ((entered_number == 0)); then
        echo "$entered_number is zero"
    else
        echo "Unkown value entered"
    fi
else
    echo "The value that you have entered is not an integer value" #Print if the value is not an integer
fi