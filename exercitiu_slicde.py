# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:58:58 2020

@author: oanap
"""
a = input('bla bla:')
b = int(input('cate litere?'))
x = len(a)
z = slice(0, b)
y = slice(x-b, x)
c = a[y]
print(c)
print(a[z])
