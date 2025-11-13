#!/bin/bash

## IS 310 Programming Challenge 4
## Author: Jack Schumacher
## Contact: js0342@uah.edu

declare -a techArray
declare -a gradeArray

# echo "Programming Challenge 6"
# echo "Please type your first and last name: "
# read -r first last
# echo "Please type the city and state that you live in (seperated by spaces):"
# read -r city state
# echo "Please type your degree and major (seperated by spaces)"
# read -r degree major
# echo "Type three favorite tech companies, with space seperating them"
# for ((i=0; i < 3; i++)); do
#     read -r -p "Enter value: " tech
#     techArray+=("$tech")
# done
# tech_array_count=${#techArray[@]}
# for((i=0;i< tech_array_count; i++)); do
#     echo "$((i+1)). ${techArray[$i]}"
# done
echo "Type 5 exam scores, seperated by spaces"
for ((i=0; i < 5; i++)); do
    read -r -p "Enter value: " grade
    gradeArray+=("$grade")
done
for i in "${gradeArray[@]}"; do
    ((sum += i))
done
count=${#gradeArray[@]}
echo $sum
average=$(echo "scale=2; $sum / $count" | bc)
echo "Average grade: $average"
