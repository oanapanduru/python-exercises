# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:26:13 2020

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
    def __str__(self):
        return 'Name: ' + self.name + ' Phone number: '+ self.phone_number
   
name = input('what is the name of the new contact you want to save?')
phone_number = input('please write the phone number:')
new_contact = Telephone(name, phone_number)
print(new_contact)
file_name = input('what is the name of the file?')
my_file = open(file_name + '.txt', 'w')
my_file.write(str(new_contact))
my_file.close()

