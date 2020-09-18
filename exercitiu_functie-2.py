# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:11:41 2020

@author: oanap
"""

lista =[1,2,3,4,5,6]
x = 6
y = len(lista)
ew = False
for i in range(y):
    print(i, lista[i], x)
    if lista[i] == x:
        ew = True
if ew == True:
    print(True)
else:
    print(False)
    

