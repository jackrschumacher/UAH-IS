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
valid_Hair_Length = len(valid_Hair)
valid_Eye = ["white", "black", "red", "green", "blue", "brown", "purple", "amber"]
valid_Eye_Length = len(valid_Eye)

character_attributes = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]
character_attributes_length = len(character_attributes)


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
            self.attributes[i] = self.attributes[i] + random.randint(1, 3)

    def add_bonus(self):
        pass


class Human(Humanoid):
    # When the user chooses a bonus attributes it will set one randomly if the user does not provide one
    def __init__(self, height, weight, race, hair_color, eye_color, bonus_attribute):
        self.bonus_attribute = (
            bonus_attribute if bonus_attribute else random.choice(character_attributes)
        )
        # Return that this user is a human and all the other attributes
        super().__init__( height, weight, "Human", hair_color, eye_color)


class Elves(Humanoid):
    def __init__(self, height, weight, race, hair_color, eye_color):
        super().__init__( height, weight, "Elves", hair_color, eye_color)

    # The Elf character adds 2 to the dexterity and charisma attributes
    def add_bonus(self):
        self.attributes["dexterity"] += 2
        self.attributes["charisma"] += 2


class Dwarf(Humanoid):
    def __init__(self, height, weight, race, hair_color, eye_color):
        # Call the Humanoid parent class and passes the updated attributes
        super().__init__( height, weight, "Dwarf", hair_color, eye_color)

    # The Dwarf character adds 2 to the strength and charisma attributes and lose 2 from the charisma attribute
    def add_bonus(self):
        self.attributes["strength"] += 2
        self.attributes["constitution"] += 2
        self.attributes["charisma"] -= 2


def create_villain():
    return "test"


# Function for creating a character- allows the user to assign traits to the character selected
def create_character():
    # TODO: Make sure that this works with characters when passing
    print("Welcome to character creation menu.")

    def select_race():
        while True:
            print(
                "Please select one of the following: \n 1. Human \n 2.Elf \n 3. Dwarf"
            )
            race_choice = input(
                "Please enter 1,2 or 3 to select the race of your character: "
            )
            try:
                race_choice = int(race_choice)
            except ValueError:
                print("Please enter a valid number")
            if race_choice == 1 or race_choice == 2 or race_choice == 3:
                if race_choice == 1:
                    race = "Human"
                    print("Thank you for your choice of: ", race)
                    return race
                elif race_choice == 2:
                    race = "Elf"
                    print("Thank you for your choice of:", race)
                    return race
                else:
                    race = "Dwarf"
                    print("Thank you for your choice of: ", race)
                    return race
            elif (race_choice != 1 or 2 or 3) and race_choice is int:
                print("Please enter a valid race")

    def select_height_weight():
        def set_height():
            while True:
                height = input(
                    "Please select a height for your character between 3 and 7 feet: "
                )
                try:
                    height = int(height)
                    if height >= 3 and height <= 7:
                        print("Thank you for selecting the height of:", height, "feet")
                        return height
                    else:
                        print("Please enter a number between 3 and 7 feet")
                except ValueError:
                    print("Please enter a valid number")

        def set_weight():
            weight = input("Please enter a weight in between 60 and 300 lbs: ")
            try:
                weight = int(weight)
                if weight >= 60 and weight <= 300:
                    print("Thank you for selecting a weight of: ", weight, "lbs")
                    return weight
                else:
                    print("Please enter a valid weight")
            except ValueError:
                print("Please enter a valid number")

        height = set_height()
        weight = set_weight()
        return height, weight

    def select_hair_eyes():
        def set_hair():
            while True:
                print(
                    "Please enter a hair color for your character from the following list:"
                )

                for i in range(valid_Hair_Length):
                    print(f"{valid_Hair[i]}")
                hair = input("Please enter your hair color:")
                try:
                    hair = str(hair)
                    hair = hair.lower()
                    if hair in valid_Hair:
                        print(
                            "Thank you for selecting the following hair color: ", hair
                        )
                        return hair
                    else:
                        print("Please enter a valid hair color")
                except ValueError:
                    print("Please enter a valid string for hair color")

        def set_eyes():
            while True:
                print(
                    "Please enter an eye color for your character from the following list:"
                )
                for i in range(valid_Eye_Length):
                    print(f"{valid_Eye[i]}")
                eyes = input("Please enter your eye color: ")
                try:
                    eyes = eyes.lower()
                    if eyes in valid_Eye:
                        print("Thank you for selecting the following eye color: ", eyes)
                        return eyes
                    else:
                        print("Please enter a valid eye color.")
                except ValueError:
                    print("Please enter a valid string for eye color")

        hair = set_hair()
        eyes = set_eyes()
        return hair, eyes

    race = select_race()
    height, weight = select_height_weight()
    hair, eyes = select_hair_eyes()

    # Check what race the user has selected and then prompt to add additional attributes depending upon user choice
    if race == "Human":
        while True:
            print(
                "As a human, you can select an attribute to add 2 bonus points to. Here are the attributes that you can choose from:"
            )
            for i in range(character_attributes_length):
                print(f"{character_attributes[i]}")
                human_bonus = input(
                    "Please enter a bonus attribute from the list above: "
                )
                try:
                    human_bonus = human_bonus.lower()
                    if human_bonus in character_attributes:
                        print(
                            "Thank you for selecting the following attribute: ",
                            human_bonus,
                        )
                        character = Human(height, weight, hair, eyes, human_bonus)
                    else:
                        print("Please enter a valid attribute.")
                except ValueError:
                    print("Please enter a valid string")

    # Do not pass bonus attributes into this class as it is handled in the function
    elif race == "Elf":
        print(
            "Elves automatically have 2 points added to both their charisma and dexterity"
        )
        character = Elves(height, weight, hair, eyes)
    # Do not pass bonus attributes into this class as it is handled in the function
    elif race == "Dwarf":
        print(
            "Dwarves automatically have 2 points added to both their strength and constitution attributes. However, Dwarves lose 2 points from their charisma attribute."
        )
        character = Dwarf(height, weight, hair, eyes)

    # Prints the character's stats to the user
    def print_stats():
        print("Character attributes: ")
        print(
            "Height: {}ft, Weight: {} lbs, Hair Color: {}, Eye Color: {}, Strength: {}, Dexterity: {}, Constitution: {}, Intelligence: {}, Wisdom: {}, Charisma: {} \n".format(
                character.height,
                character.hair_color,
                character.eye_color,
                character.attributes["strength"],
                character.attributes["dexterity"],
                character.attributes["constitution"],
                character.attributes["intelligence"],
                character.attributes["wisdom"],
                character.attributes["wisdom"],
                character.attributes["charisma"],
            )
        )

    print_stats()
    return character


# Main function for calling the other sub functions
def main():
    print("RPG Game")
    character = create_character()


main()
