# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:43:37 2020

@author: oanap
"""

exams = 3
grades = []
grades_sum = 0
for i in range(exams):
    result = int(input('what grades?'))
    grades.append(result)
for x in grades:
    grades_sum = grades_sum + x
average = grades_sum/exams
if average>= 60:
    print('you have passed')
else:
    print('you need to retake the exams')
    

