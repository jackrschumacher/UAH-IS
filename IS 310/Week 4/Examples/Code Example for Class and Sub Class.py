

class Animal:

    def __init__(self, species, age):
        self.species = species
        self.age = age

    #setters are also called mutators
    def set_species(self, species):
        self.species = species

    #getters are also called accessors
    def get_species(self):
        return self.species

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
   
#"Canis lupus familiaris"
class Dog(Animal):

    def __init__(self, species, age, name):

        Animal.__init__(self, species, age)

        self.name = name #This is public, so it CAN be changed
        self.__species = "dog" #This is private, so it can't be changed

    def description(self):
        #notice how self.__species must also be private?
        return f"{self.name} is a {self.__species} and is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

def main():

    name = input("What is your dogs name?")
    age = int(input("How old is your dog? "))
   
    your_animal = Dog(0, age, name)
    print(your_animal.description())
    print(your_animal.speak("woof woof"))

if __name__ == '__main__':
    main()