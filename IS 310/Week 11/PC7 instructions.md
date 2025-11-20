**Write a bash script that completes the following two parts.**

_**Part 1: File Operations and Permission Handling**_  

**Tasks:**

1.  Ask the user for a text file (.txt).
    *   Check whether the given file exists in the current directory
    *   Print `"Error: File is absent"` if the file is not found.
2.  If the file exists:
    *   Display its size.
    *   Check for execute permissions and print:
        *   `"You can run this file"` if the file execute permissions are enabled
        *   `"Error: You are not authorized to run this file"` if execute permissions are not enabled.
3.  Ask the user if they want to modify the file's permissions to add execute permissions.
    *   Add execute permission if the user says yes.
4.  Ask the user for their favorite movie.
    *   Append their favorite movie to the file.

_**Part 2: Directory and File Operations**_  

**Tasks:**

1.  Ask the user for a directory name and create it.
    *   If the directory already exists, print `"Directory already exists"`.
2.  Navigate to the newly created directory:
    *   Create 3 new text files named `file1.txt`, `file2.txt`, and `file3.txt` .
    *   Ask the user for their:
        *   favorite sports team and add it to `file1.txt`
        *   favorite travel destination and add it to `file2.txt`
        *   favorite food and add it to `file3.txt`
3.  Count and print the number of words in each file.
4.  Ask the user for a sub-directory name and create it.
    *   Copy one of the text files into the sub-directory
5.  Create a backup folder named `backup`
    *   Copy all files and sub-directories into the `backup` folder.
6.  Finally, compress the backup folder into a `.tar.gz` file.

_**Please submit two separate .sh files on on Canvas with the names:**_

1.  _**PC\_7\_Part\_1.sh**_
2.  _**PC\_7\_Part\_2.sh**_

**Grading Rubric:**

*   Deduct 5 points if program fails to complete all three parts as stated above.
*   Deduct 5 points if the program does not run.
*   Deduct 5 points for code without appropriate comments and pseudocode.
*   0 if code is copied from the internet or someone else's program.