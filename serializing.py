# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:49:19 2020

@author: oanap
"""


import pickle
response = input('do you want to ADD data to the file or do you want to READ the file?')
my_dictionary = {}
my_file = open('studentfile.txt', 'wb')
while response == 'add' or response =='yes':
    name =input('what is the name?')
    value = input('what score?')
    my_dictionary[name] = value
    response = input('another?')
    if response == 'no':
        pickle.dump(my_dictionary,my_file)
        response = input('do you want to read the file or exit?')
        my_file.close()
        if response == 'read':
            new_file = open('studentfile.txt','rb')
            new_dict = pickle.load(new_file)
            new_file.close()
            print(new_dict)
        else:
            break
    
    
    