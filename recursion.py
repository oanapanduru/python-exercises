# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:03:24 2020

@author: oanap
"""

def my_recursion(n):
    if n == 0:
        return 1
    else:
        return n*my_recursion(n-1)
    
n = int(input('enter a number:'))   
print(my_recursion(n))
