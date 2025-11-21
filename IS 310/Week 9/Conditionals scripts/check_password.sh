#!/bin/bash

# Check the users password and check if it matches predifined value
predifined_password="Password12345"

printf "Please enter a password: "
read entered_password
printf "\n"

if [ "$entered_password" = "$predifined_password" ]
then
    echo "Acess has been granted"
else
    echo "The password that you have entered: $entered_password has been found in the predifined passwords list"
fi