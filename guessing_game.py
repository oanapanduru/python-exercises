# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:57:51 2020

@author: oanap
"""
import random
guesses = 7
points_computer = 0
points_user = 0
x = random.randint(0, 10)
print(x)
flag = True
while flag:
    #=for i in range(guesses):
        print('enter your guess:')
        y = int(input())
        if y == x:
            print('great!')
            points_user +=1
            flag = False
            if flag == False:
                break
        print(points_user)
        else:
            if y<x:
                print('the number is higher!')
            if y>x:
                print('the number is lower!')
            points_computer +=1
print('try again?')
print('computer s points:',points_computer)
print('user s points:',points_user)

