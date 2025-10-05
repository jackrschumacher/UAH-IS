## IS 310 Programming Challenge 4
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Import random in order to randomize the additional stats (strength,charisma,etc)
import random

# Set up valid hair colors
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
# Set the length of that list
valid_Hair_Length = len(valid_Hair)
# Set valid eye colors to print out for the user when selecting
valid_Eye = ["white", "black", "red", "green", "blue", "brown", "purple", "amber"]
# Set the length of valid eye color list
valid_Eye_Length = len(valid_Eye)
# Define the global character attributes in order to use in the various functions in the program
character_attributes = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]
# Set the length of the attributes of character attributes list
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

    # Designed to randomize attack variables to simulate actual combat and luck-using random variables to change the attributes
    def combat(self, villain):
        # Modify attribute- between 5 and 10 points divided by 2 and 3
        def modify_attributes(self, attribute):
            return (
                self.attributes[attribute] - random.randint(5, 10)
            ) // random.randint(2, 3)

        # Randomly add to the strength attribute between 1 and 6 points
        attack_strength = self.attributes("strength") + random.randint(1, 6)
        combat_defense = random.randint(1, 10) + max(
            0, villain.modify_attributes("constitution")
        )
        # Determine the damage inflicted to your character depending on the attack strength
        damage_inflicted = max(0, attack_strength - combat_defense)
        # If above zero, the users character wins. If not they lose
        if damage_inflicted > 0:
            status = True
            self.increase_level()
            return status, attack_strength, combat_defense, damage_inflicted


class Human(Humanoid):
    # When the user chooses a bonus attributes it will set one randomly if the user does not provide one
    def __init__(self, height, weight, hair_color, eye_color, bonus_attribute):
        self.bonus_attribute = (
            bonus_attribute if bonus_attribute else random.choice(character_attributes)
        )
        # Return that this user is a human and all the other attributes
        super().__init__(height, weight, "Human", hair_color, eye_color)
        # Add 2 points to whatever the user wants to
        if self.bonus_attribute in self.attributes:
            self.attributes[self.bonus_attribute] += 2


class Elves(Humanoid):
    def __init__(self, height, weight, race, hair_color, eye_color):
        super().__init__(height, weight, "Elves", hair_color, eye_color)

    # The Elf character adds 2 to the dexterity and charisma attributes
    def add_bonus(self):
        self.attributes["dexterity"] += 2
        self.attributes["charisma"] += 2


class Dwarf(Humanoid):
    def __init__(self, height, weight, race, hair_color, eye_color):
        # Call the Humanoid parent class and passes the updated attributes
        super().__init__(height, weight, "Dwarf", hair_color, eye_color)

    # The Dwarf character adds 2 to the strength and charisma attributes and lose 2 from the charisma attribute
    def add_bonus(self):
        self.attributes["strength"] += 2
        self.attributes["constitution"] += 2
        self.attributes["charisma"] -= 2


def create_villain():
    return "test"


# Function for creating a character- allows the user to assign traits to the character selected
def create_character():
    print("Welcome to character creation menu.")

    # Select character race
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

    # Set character weight
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

    # Set hair color
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
                        break
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
        character.add_bonus()
    # Do not pass bonus attributes into this class as it is handled in the function
    elif race == "Dwarf":
        print(
            "Dwarves automatically have 2 points added to both their strength and constitution attributes. However, Dwarves lose 2 points from their charisma attribute."
        )
        character = Dwarf(height, weight, hair, eyes)
        character.add_bonus()

    # Prints the character's stats to the user
    def print_stats():
        print("Character attributes: ")
        print(
            "Height: {}ft, Weight: {} lbs, Hair Color: {}, Eye Color: {}, Strength: {}, Dexterity: {}, Constitution: {}, Intelligence: {}, Wisdom: {}, Charisma: {} \n".format(
                character.height,
                character.weight,
                character.hair_color,
                character.eye_color,
                character.attributes["strength"],
                character.attributes["dexterity"],
                character.attributes["constitution"],
                character.attributes["intelligence"],
                character.attributes["wisdom"],
                character.attributes["charisma"],
            )
        )

    print_stats()
    return character


# Create a villain for the main character to fight in the battle function. This function will not be displayed to the user (although this could be added easily)
def create_villain(race):
    # This class will generate the opponent attributes. Since we dont need to have the user assign the values to the opponent character, we will just randomly generate the values
    # Generate opponent height color- between 3 and 7 feet
    opponent_height = random.randint(3, 7)
    # Randomly generate opponent weight-between 60 and 300 lbs
    opponent_weight = random.randint(60, 300)
    opponent_hair = random.choice(list(valid_Hair).lower())
    opponent_eye = random.choice(list(valid_Eye).lower())
    # Randomly select a random opponent attribute to modify
    opponent_random_attribute = random.choice(character_attributes)
    if race == "Human":
        return Human(
            opponent_height,
            opponent_weight,
            opponent_hair,
            opponent_eye,
            opponent_random_attribute,
        )
    # Attributes are handled in the elf class itself, so no need to add bonus here
    elif race == "Elf":
        return Elves(opponent_height, opponent_weight, opponent_hair, opponent_eye)
    # Attributes are handled in the dwarf class itself, so no need to add bonus here
    elif race == "Dwarf":
        return Dwarf(opponent_height, opponent_weight, opponent_eye, opponent_hair)


# Main function for calling the other sub functions
def main():
    print("RPG Game")
    character = create_character()
    combat_Choice = str(
        input(
            "Would you like to enter combat with an opponent? Please enter yes and no: "
        )
    )
    if combat_Choice.lower == "yes":
        print(
            "Please select the race that you would like to combat from the following list"
        )
        print("1. Human \n 2. Elf \n 3. Dwarf")
        villain_race = str(
            input(
                "Please enter the number that corresponds with the race of the opponent that you would like to fight"
            )
        )
        while True:
            try:
                # The user chooses the human race
                if villain_race == "1":
                    villain = create_villain("Human")
                    break
                elif villain_race == "2":
                    villain = create_villain("Elf")
                    break
                elif villain_race == "3":
                    villain = create_villain("Dwarf")
                    break
                # Catch if the user enters a value out of range
                else:
                    print("Please enter a value between 1 and 3")
            # Catch if the value is not string
            except Exception as error:
                print("An error occurred while executing: ", error)

        # Print message to the user about the villain the hero
        print("Started combat between {character.race} and {opponent.race}")

        status, attack_strength, defense_strength, damage = character.combat(villain)

        if status == "won":
            print("Your character won the combat!")
            print("Your character's new attributes after combat are: ")
            # Print out the users attributes
            print(
                "Height: {}ft, Weight: {} lbs, Hair Color: {}, Eye Color: {}, Strength: {}, Dexterity: {}, Constitution: {}, Intelligence: {}, Wisdom: {}, Charisma: {} \n".format(
                    character.height,
                    character.weight,
                    character.hair_color,
                    character.eye_color,
                    character.attributes["strength"],
                    character.attributes["dexterity"],
                    character.attributes["constitution"],
                    character.attributes["intelligence"],
                    character.attributes["wisdom"],
                    character.attributes["charisma"],
                )
            )
        else:
            print("You lost the combat. Try again with a different character next time")


# Validate main function exists
if __name__ == "__main__":
    main()
