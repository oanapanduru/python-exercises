# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:47:43 2020

@author: oanap
"""
#method 1
days = 7
weather = []
for i in range(days):
    temperature = int(input('what temperature it is?'))
    weather.append(temperature)
print(weather)
weather.sort()
print(weather)
print('the coldest day was:', weather[0],'and the hottest day was:', weather[6])


#method 2
days = 7
lowest = 100
highest = 0
for i in range(days):
    print('please enter the temperature of day', i+1, ':')
    temperature = int(input())
    if temperature > highest:
        highest = temperature
        hotest= i+1
    if temperature < lowest:
        lowest = temperature
        coldest = i+1
print('the hotest day was:', hotest, 'and the coldest day was:', coldest)
