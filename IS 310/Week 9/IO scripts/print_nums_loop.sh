#!/bin/bash

# Print a list of numbers starting from 5 and going down
start_num=5

while test "$start_num" -ne 0
do
    echo "$start_num"
    # This needs to be put in to use the correct arrithmetic 
    start_num=$((start_num - 1))
done