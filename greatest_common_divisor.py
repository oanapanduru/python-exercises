# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:03:23 2020

@author: oanap
"""

def function_gcd(x,y):
  gcm = 0
  for i in range(1,y):
    if x%i == 0 and y%i == 0:
      gcm = i
  return gcm
x = int(input('what is the first number?'))
y = int(input('what is the second number?'))

print(function_gcd(x,y))

