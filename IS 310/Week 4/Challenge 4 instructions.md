### **RPG Simulator**

In this challenge, you will build an advanced RPG character creation system using Python. You will practice object-oriented programming (OOP) concepts such as class, subclass, inheritance and encapsulation. Additionally, you will work with randomness, user input validation, and simulate basic RPG mechanics like combat and levels. This program will allow players to create a character, choose a race (Human, Elf, or Dwarf), and simulate various RPG features, including character attributes, combat mechanics, and inventory management.

#### **Objectives:**

*   **Object-Oriented Programming (OOP):** You will design a superclass called Humanoid and three subclasses: Humans, Elves, and Dwarves. Each subclass will inherit from the base class and add unique features specific to that race.
    
*   **Randomization:** Use the random module to generate random attributes for each character, such as strength, dexterity, and intelligence.
    
*   **Methods:** Implement race-specific methods (e.g., bonus stats).
    
*   **Combat Simulation:** Simulate combat between characters, incorporating race-specific advantages and random elements.
    
*   **Leveling Up:** Characters will level up after combat, improving their stats and abilities.
    
*   **Input Validation:** Ensure robust user input handling for attributes like height, weight, and race selection.
    

#### **Instructions:**

1.  **Create a Base Class Humanoid:**
    
    *   Attributes for the humanoid character:
        
        *   height (in feet between 3ft and 7ft)
            
        *   weight (between 60lbs and 300lbs)
            
        *   hair\_color can be: white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde)
            
        *   eye\_color (can be: white, black, red, green, blue, brown, purple, amber)
            
        *   Random attributes for _strength, dexterity, constitution, intelligence, wisdom, and charisma_ (each between 1 and 18).
            
    *   Methods:
        
        *   combat(opponent) to simulate combat against another character.
            
        *   level\_up() to increase the character’s attributes after leveling up.
            
2.  **Create Subclasses for Different Races:**
    
    *   **Humans:**
        
        *   Humans can add +2 bonus points to any one attribute (strength, dexterity, constitution, intelligence, wisdom, or charisma).
            
    *   **Elves:**
        
        *   Elves gain +2 to both Dexterity and Charisma.
            
    *   **Dwarves:**
        
        *   Dwarves gain +2 to Strength and Constitution, but lose -2 to Charisma.
            
3.  **Character Creation:**
    
    *   Implement a character\_creation() function to allow the user to choose their race (Human, Elf, or Dwarf) and input their height, weight, hair color, and eye color.
        
    *   The character's race-specific abilities (e.g., bonus stats) should be applied based on their selection.
        
4.  **Combat System and Leveling Up:**
    
    *   Implement a combat() method in the Humanoid class that calculates damage based on the character's strength and the opponent’s defense. Use randomness to simulate the combat outcome.
        
    *   Characters should gain experience or level up after combat, improving their attributes.
        
    *   Characters will level up after each combat, improving their strength, dexterity, constitution, intelligence, wisdom, and charisma. Modify the level\_up() method for each race as needed.
        
5.  **User Interaction and Flow:**
    
    *   Implement input validation for race selection, height, weight, and other attributes to ensure the user enters valid data (e.g., valid height range, weight range, etc.).
        
    *   Implement a user-friendly interaction flow where the user is prompted for input in an engaging manner.
        
    *   Provide feedback on the character’s attributes, race-specific abilities, and combat status.
        

**Grading Rubric:**

*   deduct 5 points if program fails to create the classes an subclasses
    
*   deduct 5 points if program fails to randomize attributes and combat
    
*   deduct 5 point for code without appropriate comments and pseudocode.
    
*   deduct 5 points if program fails to run and has errors
    
*   0 if someone else's work or something from the internet or a book is submitted.
    

\=========================================================

**Sample Game Play given below for reference:**

**Welcome to Legends of Eternity. Please choose a race: Human, Elf, or Dwarf.**

*   _Enter Human, Elf, or Dwarf:_ **Human**
    
*   _Enter height (in feet between 3ft and 7ft):_ **5**
    
*   _Enter weight (between 60lbs and 300lbs):_ **120**
    
*   _Enter hair color:_ **Brown**
    
*   _Enter eye color:_ **Green**
    

**Randomly rolling stat attributes for your character**

Strength: 14, Dexterity: 7, Constitution: 5, Intelligence: 13, Wisdom: 12, Charisma: 8

*   _As a Human, you may add +2 bonus points to a single attribute (strength, dexterity, constitution, intelligence, wisdom, charisma):_ **Intelligence**
    

_**Your character's final attributes are:**_

Height: 5ft, Weight: 120lbs, Hair Color: Brown, Eye Color: Green, Strength: 14, Dexterity: 7, Constitution: 5, Intelligence: 15, Wisdom: 12, Charisma: 8

*   _Would you like to enter combat? (yes/no):_ **yes**
    
*   _Enter opponent's race:_ _**Elf**_
    

_**Combat started between Human and Elf**_

Attack strength: 16, Opponent defense: 10, Damage dealt: 6

_**You won the combat and leveled up!**_

_**Your new attributes are:**_

Strength: 15, Dexterity: 8, Constitution: 6, Intelligence: 16, Wisdom: 13, Charisma: 8