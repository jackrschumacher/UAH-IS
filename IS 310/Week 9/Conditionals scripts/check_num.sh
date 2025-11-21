#!/bin/bash

# Ask the user to input a number and check if it is greater than 10

echo "Please enter a number:"
read number
lower_limit=10

if [ "$number" -gt "$lower_limit" ]
then
    echo "The number that you have entered is greater than $lower_limit"

else
    echo "The number that you have entered is lower than or equal to $lower_limit"
fi