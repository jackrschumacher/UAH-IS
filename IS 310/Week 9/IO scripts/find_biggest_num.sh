#!/bin/bash
# Find the biggest number from a list of 3 numbers given as command line argument. Make sure errors are handled correctly.

if [ $# -ne 3 ]    
then
echo "$0: number1, number2, and number3 have not been provided"
fi
number1=$1
number2=$2
number3=$3
if [ "$number1" -gt "$number2" ] && [ "$number1" -gt "$number3" ]
then 
echo "$number1 is the biggest number"
elif [ "$number2" -gt "$number1" ] && [ "$number2" -gt "$number3" ]
then 
echo "$number2 is the biggest number"
elif [ "$number3" -gt "$number1" ] && [ "$number3" -gt "$number2" ]
then 
echo "$number3 is the biggest number"
elif [ "$number1" -eq "$number2" ] && [ "$number2" -eq "$number3" ] && [ "$number3" -eq "$number1" ]
then
echo "$number1, $number2 and $number3 are equal"
else
    echo "Unable to determine which one of the numbers provided is the largest"
fi