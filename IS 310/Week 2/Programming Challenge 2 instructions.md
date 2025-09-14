**Fun with Files**

For this programming challenge you will be working with a text file and manipulating its contents through a series of operations. Your task will involve reading from and writing to a text file, updating its contents and handling errors to ensure a smooth user experience.

Store the text file on your DESKTOP. The path should be C:\\Users\\YOUR\_USER\_NAME\\Desktop\\FunWithFiles.txt

**Program Instructions:**

1.  **File Handling and Validation:**
    
    *   Create a text file named **FunWithFiles.txt** on your Desktop, containing **exactly three lines**. Each line should have one movie title:
        
        *   _"Last of the Mohicans"_
            
        *   _"Wind River"_
            
        *   _"The Breakfast Club"_
            
    *   Your program should check if the file exists. If the file is missing, notify the user and stop further execution (_Hint: use exception handling_).
        
2.  **File Content Manipulation:**
    
    *   Once the file is validated, read the movie titles from the file.
        
    *   Display the current movie list to the user.
        
3.  **Interactive Menu:**
    
    *   Provide a menu system for the user to manage the movie list. The options should include:
        
        *   View the current movie list.
            
        *   Add a new movie to the list.
            
        *   Delete a movie from the list.
            
        *   Exit the program.
            
4.  **View the Movie list:**
    
    *   If the user chooses to view the list, print to the screen the current movie list.
        
5.  **Add a Movie:**
    
    *   If the user chooses to add a movie, prompt them to enter the name of their favorite movie.
        
    *   Append the movie title to the list.
        
6.  **Delete a Movie:**
    
    *   Allow the user to delete a movie from the list by selecting the movie number displayed in the current list.
        
7.  **Save and Exit:**
    
    *   After the user finishes modifying the movie list, save the updated list back into the original file (FunWithFiles.txt).
        
    *   Display the updated movie list before exiting.
        
8.  **Error Handling:**
    
    *   Implement proper error handling throughout the program to catch potential errors, such as file reading/writing errors, invalid inputs, and missing files.
        

**Using Functions:**

Please note that from here on out we will be using functions in all of our programs.  Therefore, your program should have the following functions for this assignments:

*   _main()_ function:
    
*   This function will call several other functions as specified by the user.
    
*   Other functions:
    
*   Some examples of functions the _main()_ function can include are the following:
    
*   _show\_movies_ function - displays current movie list
    
*   _add\_movies_ function - adds movies specified by the user
    

**Grading Rubric:**

*   Deduct 5 point from grade if the program fails to print the three original movie names to the Output Window.
    
*   Deduct 5 point for code without appropriate comments and pseudocode.
    
*   Deduct 5 points if the program fails to append the user's favorite movie choice to the text file and print the updated contents. 
    
*   Deduct 5 points if the program has a syntax error that is not fixed.
    
*   0 points if someone else's code (AI or Internet search) is used.
    

Name your assignment firstname\_lastname\_PC2.py and submit it to the Programming Challenge 2 drop box.