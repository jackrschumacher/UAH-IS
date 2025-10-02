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
        self.attributes = {
            "strength": random.randint(1, 18),
            "charisma": random.randint(1, 18),
            "dexterity": random.randint(1, 18),
            "constitution": random.randint(1, 18),
            "intelligence": random.randint(1, 18),
            "wisdom": random.randint(1, 18),
        }
        # Set the current level to 1, since we have just started the game
        self.current_level = 1

    def increase_level(self):
        # When leveling up the character add between 1 and 3 points to the list of attributes. Also increment the level
        self.current_level += 1
        for i in self.attributes:
            self.attributes[i] = self.attributes[i] + random.randint(1)

    def add_bonus(self):
        pass


class Human(Humanoid):
    # When the user chooses a bonus attributes it will set one randomly
    def __init__(self, height, weight, race, hair_color, eye_color, bonus_attribute):
        self.bonus_attribute = (
            bonus_attribute if bonus_attribute else random.choice(character_attributes)
        )
        # Return that this user is a human and all the other attributes
        super().__init__("Human", height, weight, race, hair_color, eye_color)


class Elves(Humanoid):
    def __init__(self, height, weight, race, hair_color, eye_color):
        super().__init__("Elves", height, weight, race, hair_color, eye_color)

    # The Elf character adds 2 to the dexterity and charisma attributes
    def add_bonus(self):
        self.attributes["dexterity"] += 2
        self.attributes["charisma"] += 2


class Dwarf(Humanoid):
    def __init__(self, height, weight, race, hair_color, eye_color):
        # Call the Humanoid parent class and passes the updated attributes
        super().__init__("Dwarf", height, weight, race, hair_color, eye_color)

    # The Dwarf character adds 2 to the strength and charisma attributes and lose 2 from the charisma attribute
    def add_bonus(self):
        self.attributes["strength"] += 2
        self.attributes["constitution"] += 2
        self.attributes["charisma"] -= 2


# Main function for calling the other sub functions
def main():
    print("RPG Game")


main()
