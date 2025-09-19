## Is 310- Python Project 3
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Set up the list that stores the passwords to a list
password_List = ["123456", "123456789","12345","qwerty","password","12345678","111111","123123","1234567890","1234567","qwerty123","000000","1q2w3e","aa12345678","abc123","password1","1234","qwertyuiop","123321","password123","1q2w3e4r5t","iloveyou","654321","666666","987654321","123","123456a","qwe123","1q2w3e4r","7777777","1qaz2wsx","123qwe","zxcvbnm","121212","asdasd","a123456","555555","dragon","112233","123123123","monkey","11111111","qazwsx","159753","asdfghjkl","222222","1234qwer","qwerty1","123654","123abc"]

# Check password to ensure that it is not in the common password list, and throw an error message if it is in the list and if not display a message indicating to the user that the password is strong
def check_Password(password, password_List):
    index = 0
    for value in password_List:
        index += 1
        if value == password:
            return f"The password that you entered was found in a list of commonly used passwords. It was found at index: {index}. Please consider changing it."
        else:
            validate_Password(password)
    

def validate_Password(password):
    return

def get_User_Input():
    username = str(input("Please enter your desired username"))
    password = str(input("Please enter the password that you would like to set: "))
    return password


# Get user input and pass the user-inputted password into the check_Password function, then append to the list of passwords
def main():
    print("Password and Username program")

    password = get_User_Input()
    password_Statement = check_Password(password, password_List)
    print(password_Statement)


main()