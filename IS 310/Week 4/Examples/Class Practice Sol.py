# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:36:24 2025

@author: pb0084
"""

class PlayerCharacter:
    # Initialize the PlayerCharacter with health, armor rating, and attack power.
    def __init__(self, health, armor_rating, attack_power):
        self.set_health(health)         # Set the health through the setter method
        self.set_armor_rating(armor_rating)  # Set armor rating using setter
        self.set_attack_power(attack_power)  # Set attack power using setter

    # Setter method to ensure health is within the valid range (1-100)
    def set_health(self, health):
        if 1 <= health <= 100:
            self.health = health
        else:
            print("Health must be between 1 and 100.")
            self.health = 50  # Default value if the input is invalid

    # Setter method to ensure armor rating is within the valid range (1-20)
    def set_armor_rating(self, armor_rating):
        if 1 <= armor_rating <= 20:
            self.armor_rating = armor_rating
        else:
            print("Armor rating must be between 1 and 20.")
            self.armor_rating = 10  # Default value if the input is invalid

    # Setter method to ensure attack power is within the valid range (1-20)
    def set_attack_power(self, attack_power):
        if 1 <= attack_power <= 20:
            self.attack_power = attack_power
        else:
            print("Attack power must be between 1 and 20.")
            self.attack_power = 10  # Default value if the input is invalid

    # Getter method to retrieve health
    def get_health(self):
        return self.health

    # Getter method to retrieve armor rating
    def get_armor_rating(self):
        return self.armor_rating

    # Getter method to retrieve attack power
    def get_attack_power(self):
        return self.attack_power

# Main function to interact with the user
def main():
    # Asking the user for input for each attribute
    health = int(input("Enter health (1-100): "))
    armor_rating = int(input("Enter armor rating (1-20): "))
    attack_power = int(input("Enter attack power (1-20): "))

    # Create an instance of PlayerCharacter with the user input values
    wizard = PlayerCharacter(health, armor_rating, attack_power)

    # Printing the Wizard's attributes to the console
    print("\nWizard's Attributes:")
    print(f"Health: {wizard.get_health()}")
    print(f"Armor Rating: {wizard.get_armor_rating()}")
    print(f"Attack Power: {wizard.get_attack_power()}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
