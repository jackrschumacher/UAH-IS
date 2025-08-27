## IS 310 Programming Project 1
## Author: Jack Schumacher
## Contact: js0342@uah.edu

continue_order = True
ordered_pizzas =[]
order_count = 0
user_Choice = ""
menu_Items = ["Veggie Delight", "BBQ Chicken", "Hawaiian"]

print("Python Pizza Paradise")

user_Name = str(input("Please enter your name: "))
print("Hello", user_Name +"," ,"welcome to the Python Pizza Paradise! \n")
while (continue_order == True):
    print("Select a pizza to order")
    print("Pizza Menu:")
    
    for item in menu_Items:
        print(f"{item}")
    user_Choice = str(input("Please enter the pizza that you would like to order: "))
    if(user_Choice not in menu_Items):
        print("Sorry, we only offer Veggie Delight, BBQ Chicken, or Hawaiian. Please choose again.")
    else:
        ordered_pizzas.append(user_Choice)
        print("Thank you for selecting a pizza. Would you like to order another pizza?")
        order_another = input("Enter yes or no:")
        if(order_another.lower() == "yes"):
            continue_order = True
        elif(order_another.lower() == "no"):
            continue_order = False
order_count = len(ordered_pizzas)
print("Thank you", user_Name+".","You have ordered", order_count,"pizzas. Your order will be ready in 20 minutes.")
print("You order the following pizzas:")
for orders in ordered_pizzas:
    print(f"{orders}")
