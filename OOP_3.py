# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:26:31 2020

@author: oanap
"""
class New_employee:
    def __init__(self):
        self.name = ''
        self.ID_number = ''
        self.work_shift = ''
    def set_name(self, parameter_name):
        self.name = parameter_name
    def get_name(self):
        return self.name
    def set_ID_number(self, ID_number_parameter):
        self.ID_number = ID_number_parameter
    def get_ID_number(self):
        return self.ID_number
    def set_work_shift(self, work_shift_parameter):
        self.work_shift = work_shift_parameter
    def get_work_shift(self):
        return self.work_shift
name = input('what is your name?')
ID_number = int(input('please enter your ID NUMBER:'))
work_shift = input('please enter your work shift: day shift or night shift?')
my_employee_info = New_employee()
print('Here are your employee info:')
my_employee_info.set_name(name)
print(my_employee_info.get_name())
my_employee_info.set_ID_number(ID_number)
print(my_employee_info.get_ID_number())
my_employee_info.set_work_shift(work_shift)
print(my_employee_info.get_work_shift())

