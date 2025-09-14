## IS 310 Python Project #2
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Import statements and definitions for files
import math
import os
import sys
movie_File_Path = 'C:\\Users\\jackr\\Desktop\\FunWithFiles.txt'
endProgram = False

def readMovieFile():
    
    # Check if the file exists, if not throw an error message
    if(os.path.exists(movie_File_Path)):
        movie_File = open(movie_File_Path, 'r') # Use r to tell Python that the backslashes are the literal characters
        movie_File_Contents = movie_File.read()
        print(movie_File_Contents)
        movie_File.close()
    else:
        print("The file specified does not exist. Please check the file path given")
    
# Ask the user to input a Movie to add to the list of files
def writeMovieFiles():
    if(os.path.exists(movie_File_Path)):
        movieName = str(input("Please enter a movie to add to the list of movies: "))
        addMovie = open(movie_File_Path, 'a')
        addMovie.write(f'\n{movieName}')
        addMovie.close()
        readMovieFile()
    else:
        print("The file specified does not exist. Please check the file path given.")

# Delete the movies that the user selects by converting to a list and then asking the user to select a number corresponding to a movie to delete. Error checking is implemented to ensure that the user enters valid values
def deleteMovies():
    if(os.path.exists(movie_File_Path)):
        with open(movie_File_Path, 'r') as file:
            delete_Movie_List = file.readlines()
            print(delete_Movie_List)
            cleaned_Movie_List = [s.strip() for s in delete_Movie_List]
            print(cleaned_Movie_List)
            print(len(cleaned_Movie_List))
            cleaned_List_Length = len(cleaned_Movie_List)
            for i in range(cleaned_List_Length):
                print(f"{i}. {cleaned_Movie_List[i]}")
            movie_To_Delete = int(input("What movie would you like to delete? Please enter the number of the movie you would like to delete: "))
            if(movie_To_Delete <= cleaned_List_Length and movie_To_Delete >= 0):

                delete_Movie_List.pop(movie_To_Delete)
                new_Deleted_Movie_List = "".join(map(str,delete_Movie_List))
                delete_Movie_File = open(movie_File_Path, 'w')
                delete_Movie_File.write(new_Deleted_Movie_List)
                delete_Movie_File.close()
            else:
                print("The input is not valid. The value you entered may be out of range.")
                deleteMovies()

    
        
    else:
        print("The file specified does not exist. Please check the file path given.")




# Choose the function to use, error checking is implemented to ensure that the user does not enter an invalid input
while(endProgram == False):
    print("What would you like to do?")
    print("\n 1. View the current movie list \n 2. Add a new movie to the list \n 3. Delete a movie from the list \n 4. Exit the program")
    function_Selected = input("Please enter the number corresponding with the function that you would like to execute: ")
    if(function_Selected == "1"):
        readMovieFile()
    elif(function_Selected == "2"):
        writeMovieFiles()
    elif(function_Selected == "3"):
        deleteMovies()
    elif(function_Selected == "4"):
        endProgram == True
        print("Thank you for using the movie list program. Here is the list of movies saved:")
        readMovieFile()
        sys.exit(0)
    else:
        print("Please enter a valid option.")
        