#!/bin/bash

## IS 310 Programming Challenge 6
## Author: Jack Schumacher
## Contact: js0342@uah.edu

declare -a techArray
declare -a gradeArray

echo "Programming Challenge 6"
echo "Please type your first and last name: "
read -r first last
if [[ -n "$first" && -n "$last" ]]; then
    echo "Your name is: $first $last"
else
    echo "You did not enter a value"
fi
echo "Please type the city and state that you live in (seperated by spaces):"
read -r city state
if [[ -n "$city" && -n "$city" ]]; then
    echo "You live in $city, $state"
else
    echo "You did not enter a value"
fi
echo "Please type your degree and major (seperated by spaces)"
read -r degree major
if [[ -n "$degree" && -n "$major" ]]; then
    echo "Your degree is $degree and your major is $major"
else
    echo "You did not enter a value"
fi
echo "Type three favorite tech companies, with space seperating them"
for ((i=0; i < 3; i++)); do
    read -r -p "Enter value: " tech
    if [[ -n "$tech" ]]; then
        techArray+=("$tech")
    else
        echo "You did not enter a value"
        i=$((i-1))
    fi
    
done
tech_array_count=${#techArray[@]}
echo "You like the following tech companies"
for((i=0;i< tech_array_count; i++)); do
    echo "$((i+1)). ${techArray[$i]}"
done
echo "Type 5 exam scores, seperated by spaces"
for ((i=0; i < 5; i++)); do
    read -r -p "Enter value: " grade
    
    if [[ -n "$grade" ]]; then
        gradeArray+=("$grade")
    else
        echo "You did not enter a value"
        i=$((i-1))
    fi
done
for i in "${gradeArray[@]}"; do
    ((sum += i))
done
count=${#gradeArray[@]}
# Use the basic calculator utility to get a more accurate value
average=$(echo "scale=2; $sum / $count" | bc) 
echo "Average grade: $average"
printf "Please enter a sentance to describe your major: "
read major_description
echo "$major_description" > major_description.txt