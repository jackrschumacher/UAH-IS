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


def main():
    print("RPG Simulator")
