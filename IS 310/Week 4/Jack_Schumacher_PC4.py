## IS 310 Programming Challenge 4
## Author: Jack Schumacher
## Contact: js0342@uah.edu


# Imports
import random


# Initialize Humanoid class with attributes
class Humanoid:
    def __init__(
        self,
        height,
        weight,
        hair_color,
        eye_color,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
    ):
        self.set_Height(height)
        self.set_Weight(weight)
        self.set_Hair_Color(hair_color)
        self.set_Eye_Color(eye_color)
        self.set_Strength(strength)
        self.set_Dexterity(dexterity)
        self.set_Constitution(constitution)
        self.set_Intelligence(intelligence)
        self.set_Wisdom(wisdom)
        self.set_Charisma(charisma)

        def set_Height(self, height):
            # Set user inputted height value if the value is within the desired range
            if height >= 3 and height <= 7:
                self.height = height
            # Set the default height value at 5 feet if the user input is invalid
            else:
                print(
                    "Your height must be between 3 and 7 feet. Your height has been assigned at 5 feet"
                )
                self.height = 5

        def set_Weight(self, weight):
            if weight >= 60 and weight <= 300:
                self.weight = weight
            else:
                print(
                    "Your weight value must be in between 60 and 300 pounds. Your weight has been set at 150 pounds"
                )
                self.weight = 150

        # TODO: Make sure that these lists can be read in upper/lowercase
        def set_Hair_Color(self, hair_color):
            valid_Hair_Color = [
                "white",
                "silver",
                "gray",
                "brown",
                "green",
                "blue",
                "yellow",
                "pink",
                "red",
                "blonde",
            ]
            if hair_color in valid_Hair_Color:
                self.hair_color = hair_color
            else:
                self.hair_color = random.choice(valid_Hair_Color)
                print(
                    "You have selected a hair color that is not valid. Your hair color has been set as: ",
                    self.hair_color,
                )

        def set_Eye_Color(self, eye_color):
            valid_Eye_Color = [
                "white",
                "black",
                "red",
                "green",
                "blue",
                "brown",
                "purple",
                "amber",
            ]
            if eye_color in valid_Eye_Color:
                self.eye_color = eye_color
            else:
                self.eye_color = random.choice(valid_Eye_Color)
                print(
                    "You have selected an eye color that is not valid. Your eye color has been set as: ",
                    self.eye_color,
                )

        def set_strength(self, strength):
            if strength >= 1 and strength <= 18:
                self.strength = strength
            else:
                self.strength = random.randint(1, 18)
                print(
                    "You have entered a strength value outside of the range of 1 to 18. Your strength has been set at",
                    self.strength,
                )

        def set_constitution(self, constitution):
            if constitution >= 1 and constitution <= 18:
                self.constitution = constitution
            else:
                self.constitution = random.randint(1, 18)
                print(
                    "You have entered a constitution value outside of the range of 1 to 18. Your constitution has been set at",
                    self.constitution,
                )

        def set_intelligence(self, intelligence):
            if intelligence >= 1 and intelligence <= 18:
                self.intelligence = intelligence
            else:
                self.intelligence = random.randint(1, 18)
                print(
                    "You have entered a intelligence value outside of the range of 1 to 18. Your intelligence has been set at",
                    self.intelligence,
                )

        def set_dexterity(self, dexterity):
            if dexterity >= 1 and dexterity <= 18:
                self.dexterity = dexterity
            else:
                self.dexterity = random.randint(1, 18)
                print(
                    "You have selected a dexterity value that is not between 1 and 18. Your dexterity has been set at: ",
                    self.dexterity,
                )

        def set_wisdom(self, wisdom):
            if wisdom >= 1 and wisdom <= 18:
                self.wisdom = wisdom
            else:
                self.wisdom = random.randint(1, 18)
                print(
                    "You have selected a wisdom value that is not between 1 and 18. Your wisdom has been set at: ",
                    self.wisdom,
                )

        def set_charisma(self, charisma):
            if charisma >= 1 and charisma <= 18:
                self.charisma = charisma
            else:
                self.charisma = random.randint(1, 18)
                print(
                    "You have selected a charisma value that is not between 1 and 18. Your charisma has been set at: ",
                    self.charisma,
                )

        def combat():
            print("Test")

        def level_up():
            print("Test")

class Human(Humanoid):
    print("Test")

class Elf(Humanoid):
    print("x")
class Dwarves(Humanoid):
    print("x")

def character_creation():
    print("Please select a character from the following list: \n 1.Human \n 2.Elf \n 3. Dwarves")
    character_Choice_Number = input("Please enter the number corresponding")
    if(character_Choice_Number >=1 and character_Choice_Number <= 3):
        if(character_Choice_Number == 1):
            default_attributes()
            print("As a human, you can add 2 points to an attribute of your choosing. Select from any of the following attributes:")
        elif(character_Choice_Number ==2):
            print("As an elf")
            default_attributes()
        else:
            default_attributes()

    else:
        print("The number that you entered was not valid. Please try again")
        character_creation()

    def default_attributes():

    


def main():
    print("RPG Simulator")
    character_creation()