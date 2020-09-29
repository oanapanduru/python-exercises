# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:32:29 2020

@author: oanap
"""


class My_animals:
    def __init__(self, animal_name):
        self.animal_name_atr = animal_name
    def animal_type(self, parameter_animal_type):
        self.animal_type = parameter_animal_type
    def show_name(self):
        return self.animal_name_atr
    def show_type(self):
        return self.animal_type
print('what is the name of the animal?')
name = input()
my_pet = My_animals(name)
print('your pet s name is:')
print(my_pet.show_name())

print('what type is your animal?')
type_name = input()
my_pet.animal_type(type_name)
print('your pet s type')
print(my_pet.show_type())
