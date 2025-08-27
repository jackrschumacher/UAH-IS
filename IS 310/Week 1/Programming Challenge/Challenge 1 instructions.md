For this challenge, you will be writing a program that uses the topics introduced in the previous lectures. For your reference, they are Input, Processing, and Output, Decision Structures and Boolean Logic, Repetition Structures, and Input Validation.

Instructions:  Write a program in Python that performs the following actions:

**Introduction and User Interaction:**

* Ask the user to enter their name.
* Print a welcome message to the user:
```"Hello [user's name], welcome to the Python Pizza Paradise!" ```

**Pizza Selection:**

* Present a menu with the following types of pizzas: Veggie Delight, BBQ Chicken, and Hawaiian.
* Ask the user to choose which pizza they would like to order by typing one of the pizza types listed above.
* If the user enters anything that is not a valid option (such as "Pepperoni"), print this message: ```"Sorry, we only offer Veggie Delight, BBQ Chicken, or Hawaiian. Please choose again."```
  
**Order More or Not:**

* Once the user selects a pizza, ask them if they want to order another pizza. The user can answer "yes" or "no".
* If they enter "yes", allow them to choose another pizza.
* If they enter anything other than "yes" or "no", print the message: ```"Please answer with 'yes' or 'no' only."```
* Continue prompting the user for additional pizza orders until they type "no".

**Final Order Summary:**

* Once the user decides they are done ordering, print a message like: ```"Thank you [user's name]. You have ordered [number of pizzas ordered] pizzas. Your order will be ready in 20 minutes!"```

**Additional Requirements:**

* Use a while loop to allow the user to continue ordering pizzas until they say "no".
* Use input validation to ensure the user chooses a valid pizza type.
* Ensure the user's input is case insensitive when confirming their order of "yes" or "no".
* Count the total number of pizzas ordered and print it in the order message.

**Grading Criteria:**

Your program will be graded with the following rubric:
* -50 points if the program is submitted with errors (meaning it does not run)
* -10 points for each Programming Concept that is not implemented in the program. Refer to the above section for concepts that need to be implemented.
* 0 if someone else’s work or copy a similar program from the internet is submitted.

**Submission Process:**

Name the file your_Name_PC_1.py

Please submit the .py file to the Programming Challenge 1 drop-box in Canvas.