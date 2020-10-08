# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:19:43 2020

@author: oanap
"""


class Telephone:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    def get_name(self):
        return self.name
    def get_phone_number(self):
        return self.phone_number
   
name = input('what is the name of the new contact you want to save?')
phone_number = input('please write the phone number:')
new_contact = Telephone(name, phone_number)
print(new_contact.get_name(), new_contact.get_phone_number())
file_name = input('what is the name of the file?')
my_file = open(file_name + '.txt', 'w')
my_file.write(str(new_contact.get_name()))
my_file.write(':')
my_file.write(str(new_contact.get_phone_number()))
my_file.close()
    