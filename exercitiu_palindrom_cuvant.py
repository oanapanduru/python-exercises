# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:50:31 2020

@author: oanap
"""
#Sa se scrie o functie care primeste un text ca parametru si verifica daca
# acesta este palindrom. Functia va returna True sau False daca textul este sau
# nu palindrom.

def cuvant_palindrom(a):
    x = len(a)
    y = ''
    while x > 0:
        y = y + a[x-1]
        x -=1
    if a == y:
        return True
    else:
        return False
print(cuvant_palindrom('aba'))


