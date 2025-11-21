#!/bin/bash

## IS 310 Programming Challenge #7 Part 2
## Author: Jack Schumacher
## Contact: js0342@uah.edu

read -p "Please enter a name of the directory" directory
# Check if the directory exists. If so naviagte into it. If not create and navigate it
if [[ -d "$directory" ]]; then
    echo "The directory specified already exists"
    cd $directory
else
    echo "Creating the directory $directory"
    mkdir $directory
    cd $directory

fi
# Create 3 txt files and then create variables
touch file1.txt file2.txt file3.txt
read -p "What is your favorite sports team: " sports_team
read -p "What is your favorite travel destination: " travel_destination
read -p "What is your favorite food: " favorite_food
# Write to file
echo "$sports_team" >> file1.txt
echo "$travel_destination" >> file2.txt
echo "$favorite_food" >> file3.txt
# Get word counts of files
echo "Word count per file:"
wc -w file1.txt
wc -w file2.txt
wc -w file3.txt
# Create a subdirectory
read -p "Please enter a name to create a sub directory: " sub_directory
mkdir $sub_directory
cp file1.txt $sub_directory
# Create the backup directory and create a .tar.gz
mkdir backup
cp -r . backup
tar -czvf backup.tar.gz backup
