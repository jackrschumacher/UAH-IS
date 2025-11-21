#!/bin/bash

# Check the users age and tell them wether they are an adult based upon thier age (greater than 18)

echo "Please input your age"
read age
adult_age=18

if [ "$age" -gt "$adult_age" ]
then
    echo "You are an adult"
else
    echo "You are not an adult"
fi