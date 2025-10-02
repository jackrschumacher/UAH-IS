## IS 310 Programming Challenge 4
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Import random in order to randomize the additional stats (strength,charisma,etc)
import random
valid_Hair = [
    "white",
    "silver",
    "gray",
    "black",
    "green",
    "blue",
    "pink",
    "red",
    "blonde",
]
valid_eye = ["white", "black", "red", "green", "blue", "brown", "purple", "amber"]
character_attributes = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]


class Humanoid:

    # Create the character and the attributes of the character
    def __init__(self, height, weight, race, hair_color, eye_color):
        self.height = height
        self.weight = weight
        self.race = race
        self.hair_color = hair_color
        self.eye_color = eye_color

        # Create a list of the attributes that the character has- these are the ones that are randomly assigned
        self.attributes ={
            "strength": random.randint(1,18),
            "charisma": random.randint(1,18),
            "dexterity": random.randint(1,18),
            "constitution": random.randint(1,18),
            "intelligence": random.randint(1,18),
            "wisdom": random.randint(1,18)
        }
        # Set the current level to 1, since we have just started the game
        self.current_level = 1 

class Human(Humanoid):
    # When the user chooses a bonus attributes it will set one randomly
    def  __init__(self, height, weight, race, hair_color, eye_color, bonus_attribute):
        self.bonus_attribute = bonus_attribute if bonus_attribute else random.choice(character_attributes)
        
# Main function for calling the other sub functions
def main():
    print("RPG Game")
main()