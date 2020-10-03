# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:44:40 2020

@author: oanap
"""
class New_employee:
    def __init__(self, name, ID_number, work_shift):
        self.name = name
        self.ID_number = ID_number
        self.work_shift = work_shift
    def get_name(self):
        return self.name
    def get_ID_number(self):
        return self.ID_number
    def get_work_shift(self):
        return self.work_shift
name = input('what is your name?')
ID_number = int(input('please enter your ID NUMBER:'))
work_shift = input('please enter your work shift: day shift or night shift?')
my_employee_info = New_employee(name,ID_number, work_shift)
print('Here are your employee info:')
print(my_employee_info.get_name())
print(my_employee_info.get_ID_number())
print(my_employee_info.get_work_shift())

