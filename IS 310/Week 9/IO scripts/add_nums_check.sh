#!/bin/bash
#Add two numbers if provided, if not provided, throw an error.
# The numbers are provided in the shell Like: ./add_nums_check 1 2 (this would print 3)
if [ $# -ne 2 ]
then
    echo "Usage - $0  x  y"
    echo "      Where x and y are two numbers which will print the sum"
    exit 1

fi
    echo "Sum of $1 and $2 is `expr $1 + $2`"
