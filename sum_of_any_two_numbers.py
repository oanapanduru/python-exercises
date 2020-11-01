# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:41:09 2020

@author: oanap
"""
my_list = [1, 4, 5, 8, 9, 1, 13, 6]
k = 9
l = len(my_list)
flag = False
for i in range(0,l):
    for x in range(i+1,l-1):
        if my_list[i]+ my_list[x] == k:
            print(True)
            print(my_list[i], '',my_list[x])
            flag = True
            break
    if flag == True:
        break
if flag == False:
    print(False)
