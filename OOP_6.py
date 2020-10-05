# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:50:30 2020

@author: oanap
"""

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
 
def again_function(grocery_list):
    answer = input('do you want to add something else?')
    while answer == 'yes':
        main(grocery_list)
        answer = input('do you want to add something else?')
    else:
        print('here is your grocery list:')
        for i in grocery_list:
            print(i.get_name(),'-', i.get_price(), '$')

def main(grocery_list):
    name = input('what fruit do you want to buy?')
    price = input('what is the price?')
    my_fruit = Fruit(name,price)
    grocery_list.append(my_fruit)
    for i in grocery_list:
        print(i.get_name(), '-', i.get_price(),'$')
grocery_list = []
main(grocery_list)
again_function(grocery_list)