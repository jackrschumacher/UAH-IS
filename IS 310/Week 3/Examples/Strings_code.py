# -*- coding: utf-8 -*-
"""
Module - Strings
@author: prs
"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#searching for a value in the string
char = input("What letter would you like to search for? ")

if char in letters:
    print(f"the letter {char} was found in the string")

else:
    print("The letter was not found in the string")
    

#accessing a specific index value in the string
element = letters[5]
index = letters.index(char)
print(f'The element {element} is located at index {index}')

#concatenating strings
numbers = '123456'

combined = numbers + letters
print(combined)

#slicing strings
first_half = letters[0:13] 
second_half = letters[13:]
print(first_half, second_half)

#the FIND method
phrase = "99 Red ballons"
position = phrase.find("Red")

if position != -1:
    
    print(f"The word was contained at position {position}")

else:
    print("The word was not found")
    
#determining the type of file by using the endswith substring
filename = input("")

if filename.endswith('.txt'):
    print("The file you are looking for is a text file")

else:
    print("The file is not a text file")
    
#replacing values
newPhrase = phrase.replace("ballons", "apples")
print(newPhrase)

#converting the letters above into all lower case letters
result = letters.lower()
print(result)