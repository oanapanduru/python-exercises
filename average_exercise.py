# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:40:53 2020

@author: oanap
"""
number_of_exams = int(input('how many exams?'))
grades_list = []
for i in range(number_of_exams):
    result = int(input('the result of the exam:'))
    grades_list.append(result)
suma = 0
for x in grades_list:
    suma = suma + x
    print(x)
average = suma/number_of_exams
print(average)

