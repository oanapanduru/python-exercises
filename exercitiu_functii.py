# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:07:01 2020

@author: oanap
"""
#Sa se scrie o functie care primeste un text ca parametru si returneaza textul scris
#invers.
	#Ex: reverse_function(“casa”) va returna “asac”
def cuvant_invers(a):
    x = len(a)
    y = ''
    while x > 0:
        y = y + a[x-1]
        x -=1
    return y
print(cuvant_invers('inghetata'))


