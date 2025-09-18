**Python Password Management System**

For this challenge, you will be creating a Python program that manages a password database and performs password validation using advanced techniques. The program will store a list of 50 common passwords, validate user passwords, and provide feedback accordingly. You will utilize regular expressions for password validation, error handling, and modular programming practices.

**Assignment Requirements:**

1.  **Password List Storage**:Store 50 common passwords in a list (the list is provided below).
    
2.  **Password Check**:Ask the user to create a username and password.
    
    *   Check if the user’s password exists in the list of common passwords (Hint: use a looping structure or the **in** operator)
        
    *   If the password is found, print the following message along with its index:_“Your password is too common. It was found at index_ _**X**__. Please consider changing it.”_
        
    *   If the password is not in the list, proceed to the next step for validation.
        
3.  **Password Validation**:If the password is not in the list of common passwords, you will validate it against the following security criteria:
    
    *   It must contain at least **one uppercase letter**.
        
    *   It must contain at least **one lowercase letter**.
        
    *   It must contain at least **one number**.
        
    *   It must contain at least **one special character from the following list:** _**#, $, \_, -, +, =.**_
        
    *   The password must be **at least 8 characters** long.
        
4.  **Password Strength Confirmation**:If the _password meets the criteria_, append it to a new password list called _**strong\_password**_ and print:“_You have a strong password.”_If the _password does not meet the criteria_, **ask the user to create a new password** until it is valid.
    
5.  **Error Handling**:Make sure that the user cannot bypass the validation process, and handle any potential errors gracefully (input validation).
    

**Program Instructions:**

*   **Create a list of 50 common passwords**. This list is provided at the end of this instruction.
    
*   *   **check\_password(password, password\_list)** that:
        
        *   Compares the user’s password with the common passwords list.
            
        *   If the password is found, return the message indicating the index at which it is found.
            
        *   If the password is not found, return the message indicating a strong password.
            
    *   **validate\_password(password)** that:
        
        *   Ensures the password meets the following criteria using regular expressions:
            
            *   At least one uppercase letter.
                
            *   At least one lowercase letter.
                
            *   At least one digit.
                
            *   At least one special character from the set #, $, \_, -, +, =.
                
            *   A minimum length of 8 characters.
                
    *   **get\_user\_input()** that:
        
        *   Prompts the user for a username and password.
            
        *   Ensures that the password is validated according to the requirements.
            
    *   **main() function** that:
        
        *   Calls get\_user\_input() to get the user’s username and password.
            
        *   Passes the password to check\_password() to check if it is in the list of common passwords.
            
        *   If the password is valid, append it to the password list and print the message:“You have a strong password.”
            

**Programming Constructs Used:**

*   Lists
    
*   Loops (probably a for loop for this) IF you don't use the **in** operator
    
*   In operator
    
*   Decision Structures (IF, ELIF, ELSE)
    
*   Comparing strings
    
*   processing input
    
*   Index location
    

**Grading Rubric:**

*   deduct 5 points if program fails to pass an argument and return the value back to getUserPass()
    
*   deduct 5 points if program fails to print the location of the password IF it is found in the list
    
*   deduct 5 points if program fails to properly confirm the user's password and a password in the list match
    
*   deduct 5 point for code without appropriate comments and pseudocode.
    
*   0 if someone else's work or something from the internet or a book is submitted.
    

**Password List (used in the List separated by commas):**

1.  123456
    
2.  123456789
    
3.  12345
    
4.  qwerty
    
5.  password
    
6.  12345678
    
7.  111111
    
8.  123123
    
9.  1234567890
    
10.  1234567
    
11.  qwerty123
    
12.  000000
    
13.  1q2w3e
    
14.  aa12345678
    
15.  abc123
    
16.  password1
    
17.  1234
    
18.  qwertyuiop
    
19.  123321
    
20.  password123
    
21.  1q2w3e4r5t
    
22.  iloveyou
    
23.  654321
    
24.  666666
    
25.  987654321
    
26.  123
    
27.  123456a
    
28.  qwe123
    
29.  1q2w3e4r
    
30.  7777777
    
31.  1qaz2wsx
    
32.  123qwe
    
33.  zxcvbnm
    
34.  121212
    
35.  asdasd
    
36.  a123456
    
37.  555555
    
38.  dragon
    
39.  112233
    
40.  123123123
    
41.  monkey
    
42.  11111111
    
43.  qazwsx
    
44.  159753
    
45.  asdfghjkl
    
46.  222222
    
47.  1234qwer
    
48.  qwerty1
    
49.  123654
    
50.  123abc