# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:50:37 2020

@author: oanap
"""
#method 1
print('the first 8 Fibonacci numbers are:')
a = 0
b = 1
print(a)
print(b)
for i in range(6):
    c = a + b
    a = b
    b = c
    print(c)
    
#method 2
a = 0
b = 1 
x = 3
print(a)
print(b)
def fibonacci(a,b,x):
    if x <= 8:
        c = a+b
        print(c)
        fibonacci(b,c,x+1)
        
fibonacci(a,b,x)


