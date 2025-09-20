## Is 310- Python Project 3
## Author: Jack Schumacher
## Contact: js0342@uah.edu


# Set up the list that stores the passwords to a list
password_List = ["123456", "123456789","12345","qwerty","password","12345678","111111","123123","1234567890","1234567","qwerty123","000000","1q2w3e","aa12345678","abc123","password1","1234","qwertyuiop","123321","password123","1q2w3e4r5t","iloveyou","654321","666666","987654321","123","123456a","qwe123","1q2w3e4r","7777777","1qaz2wsx","123qwe","zxcvbnm","121212","asdasd","a123456","555555","dragon","112233","123123123","monkey","11111111","qazwsx","159753","asdfghjkl","222222","1234qwer","qwerty1","123654","123abc"]
strong_Password_List = []
# Check password to ensure that it is not in the common password list, and throw an error message if it is in the list and if not display a message indicating to the user that the password is strong
def check_Password(password, password_List, username):
    index = 0
    for value in password_List:
        index += 1
        if value == password:
            return f"The password that you entered was found in a list of commonly used passwords. It was found at index: {index}. Please consider changing it."
    validated_Statement = validate_Password(password)

    if validated_Statement == True:
        strong_Password_List.append(password)
        return f"Congratulations! You have set your username: {username} and your password: {password}"
    else:
         return "Your password is invalid. It must contain the following: \n 1. One or more uppercase letter \n 2. One or more lowercase letter \n 3. One or more digits \n 4. One special character (#,$,_,-,+) \n 5. A minimum length of 8 characters"


# Set up a variety of flags that that trigger when a part of the string matches the conditions specified in the instructions for the project. Once all conditions are met, return true
def validate_Password(password,):
    
    has_Character = False
    has_Upper = False
    has_Lower = False
    has_Digit = False
    has_Special_Character = False
    
    if len(password) >= 8:
        has_Character = True
        
    for value in password:
        if value.isupper():
            has_Upper = True
        elif value.islower():
            has_Lower = True
        elif value.isdigit():
            has_Digit = True
        elif value in "#$_-+=":
            has_Special_Character = True
    if has_Character == True and has_Upper == True and has_Lower == True and has_Digit == True and has_Special_Character == True:
        return True
    else:
        return False

        
 
  
        
# Ask the user to input their username and password, return username and password
def get_User_Input():
    username = str(input("Please enter your desired username: "))
    password = str(input("Please enter the password that you would like to set: "))
    return password, username


# Get user input and pass the user-inputted password into the check_Password function, then append to the list of passwords
def main():
    print("Password and Username program")

    password, username = get_User_Input()
    password_Statement = check_Password(password, password_List,username)
    # Call if password not valid
    if password_Statement == "Your password is invalid. It must contain the following: \n 1. One or more uppercase letter \n 2. One or more lowercase letter \n 3. One or more digits \n 4. One special character (#,$,_,-,+) \n 5. A minimum length of 8 characters":
        print(password_Statement)
        password, username = get_User_Input()
        password_Statement = check_Password(password, password_List,username)
        print(password_Statement)
    # If the password is valid, then print the username and password combo
    else:
        print(password_Statement)

# Call main function
main()