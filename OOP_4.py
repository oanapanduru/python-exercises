# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:51:08 2020

@author: oanap
"""
class Cars:
    def __init__(self, name, year):
       prius={2014:10000, 2015:12000, 2016:14000, 2017:20000, 2018:28000}
       camry={2014:13000, 2015:16000, 2016:20000, 2017:23000, 2018:28000} 
       highlander={2014:15000, 2015:19000, 2016:22000, 2017:26000, 2018:32000}

       if model=='prius':
            self.price=prius[year]
       elif model=='camry':
            self.price=camry[year]
       else:
            self.price=highlander[year]
    def get_price(self):
         return self.price
     
model = input('what Toyota model do you want: PRIUS, CAMRY, HIGHLANDER?')
year_of_make = int(input('what year of make: 2014-2018?'))
my_car = Cars(model, year_of_make)
print(my_car.get_price())

my_car_2 = Cars('camry', 2017)
print(my_car_2.get_price())




