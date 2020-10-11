# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:19:33 2020

@author: oanap
"""
class Description:
    def __init__(self, p_year_of_make, p_model, p_miles):
        self.year_of_make = p_year_of_make
        self.model = p_model
        self.miles = p_miles
    def get_year_of_make(self):
        return self.year_of_make
    def get_model(self):
        return self.model
    def get_miles(self):
        return self.miles

class Price(Description):
    def __init__(self, p_year_of_make, p_model, p_miles, p_price):
        Description.__init__(self, p_year_of_make, p_model, p_miles)
        self.price = p_price
    def get_price(self):
        return self.price
    
def main():
    print('please enter below the description of the car:')
    p_year_of_make = input('enter the year of make:')
    p_model = input('enter the model:')
    p_miles = input('enter the miles:')
    
    general_description = Description(p_year_of_make, p_model, p_miles)
    print('year of make:',general_description.get_year_of_make())
    print('model:', general_description.get_model())
    print('miles:', general_description.get_miles())
    return general_description
 

def price_function():
    general_description = main()
    response = input('do you also want to add details of the price?')
    if response == 'yes':
        p_price = input('enter the price:')
        general_description_price = Price(general_description.get_year_of_make(), general_description.get_model(), general_description.get_miles(), p_price)
        print('here is the complete description:')
        print('year of make:',general_description_price.get_year_of_make())
        print('model:', general_description_price.get_model())
        print('miles:', general_description_price.get_miles())
        print('price:',general_description_price.get_price())
             
    else:
        print('year of make:',general_description.get_year_of_make())
        print('model:', general_description.get_model())
        print('miles:', general_description.get_miles())
price_function()

