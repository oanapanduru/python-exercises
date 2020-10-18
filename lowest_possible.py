# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:50:15 2020

@author: oanap
"""
elements = int(input('how many elements do you want to add to the list?'))
my_list = []
for i in range(elements):
    numbers =int(input('please enter the number:'))
    my_list.append(numbers)
print(my_list)

lowest = my_list[0]
highest = my_list[0]
for x in my_list:
    if x < lowest and x>0:
        lowest = x
    if x > highest and x>0:
        highest = x
if lowest > 1 or highest <1:
    lowest = 1
    print(lowest)
else: 
    flag = False
    new_lowest = None
    for x in range(1,highest):
        if x not in my_list:
            flag = True
            new_lowest = x
            print(new_lowest)
            break
    if flag == False:
        new_lowest = highest+1
        print(new_lowest)
    
        
            
    

    
