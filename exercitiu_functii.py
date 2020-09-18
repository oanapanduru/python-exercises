# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:07:01 2020

@author: oanap
"""
#write a function that receives a text as a parameter and return the text reversed.

def cuvant_invers(a):
    x = len(a)
    y = ''
    while x > 0:
        y = y + a[x-1]
        x -=1
    return y
print(cuvant_invers('inghetata'))


