import random
correct_number = random.randint(1,50)
userGuess = 0
num_guesses = 0
correct_range_upper = correct_number +5
correct_range_lower = correct_number - 5
while(userGuess != correct_number):
    print("You have used", num_guesses, "guesses")
    userGuess = int(input("Please enter a number between 1 and 50: "))
    if(userGuess > 50 or userGuess <1):
        print("Please try again with a value greater than 1 and less than 50")
    elif(userGuess <= correct_range_upper and userGuess >= correct_range_lower):
        print("Your guess is within 5 numbers of the correct value")
    num_guesses += 1


print("You have guessed the correct answer. ")
print("It took you", num_guesses, "guesses")