# -*- coding: utf-8 -*-
"""
Module - Object Oriented Programming
@author: prs
"""

class Bicycle:
    
    def __init__(self, gear, speed):
        
        self.__gear = gear
        self.__speed = speed
        
    def set_gear(self, gear):
        self.__gear = gear
        
    def set_speed(self, speed):
        self.__speed = speed
        
    def get_gear(self):
        return self.__gear
    
    def get_speed(self):
        return self.__speed
    
#import Bicycle
#use the import if you built the class in another file, which is the proper 
#way to use classes in OOP
def bicycleState():
    
    spd = int(input("How fast is the bicycle traveling in MPH: "))
    gr = int(input("What gear is the bicycle currently in (1-4): "))

    #create and instance of the Bicyce class
    bike = Bicycle(gr, spd)
    #Use the below code if importing from another class.   
    #bike = bicycle.Bike(gr, spd)
    print(f'The bicycle is in gear {bike.get_gear()} and is traveling at {bike.get_speed()} mph')
if __name__ == '__main__':
    
    bicycleState()