#!/bin/bash

# Write a Bash script that checks if a user is logged in and if they are, prints their username, otherwise prints "User is not logged in".

echo "Login checker"
printf "Please enter your username: "
read username

# Check if value entered is non-empty
if [[ -n "$username" ]]; then
    # "who" displays what user is currently logged into the system
    if who | grep -q "^$username";then
        echo "$username is currently logged in"
    else
        echo "$username is not currently logged in"
    fi
else
    echo "The value entered is empty"
fi