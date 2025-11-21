#!/bin/bash

## IS 310 Programming Challenge #7 Part 1
## Author: Jack Schumacher
## Contact: js0342@uah.edu

echo "Programming challenge 7"
echo "Please enter a file name: "
read -r filename
if [[ -f  "$filename" ]]; then # The f argument ensures that they have entered a file, not a directory
    echo "The file $filename exists in the current directory"
    filesize=$(stat -c %s $filename)
    echo "The file contains: $filesize bytes"
    if [[ -x $filename ]];then
        echo "You have the permssions to execute $filename" # If user can execute file
    else # Tell the user that they do not have the permission to execute the file
        echo "Error: You do not have the permissions to execute $filename"
        expected_value="yes"
        read -p "Would you like to add execute permissions to $filename? Type yes: " execute
        if [[ "${execute,,}" == "$expected_value" ]];then #Allow for non-precise matchin of input
            echo "Execute permissions granted"
            chmod +x "$filename" #Add execute permissions to the file
        else
            echo "No execute permissions granted to $filename as the file is already executeable" #Tell user that the file is already executeable
        fi
    fi
    # Append the movie name to the filename
    read -p "What is the name of your favorite movie: " movie
    echo "$movie" >> "$filename"
    echo "Appended $movie to $filename"
else #Error catch if the filename does not exist in the present directory
    echo "The file $filename does not exist in the current directory"
fi
