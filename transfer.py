# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:25:13 2020

@author: oanap
"""
#question =input('do you want to add money batches or you want to transfer money batches?')
#account = 0
#money = 0

question =input('do you want to add money batches or you want to transfer money batches?')

def transfer():
    number = int(input('how many batches do you want to transfer?'))
    account = 0
    for i in range(number):
        money = int(input('how much?'))
        account = account + money
    print('you have transfered',account, 'from your account')
    question=input('do you want to transfer more money batches?')
    return question
      
            
if question == 'add':
    number = int(input('how many batches?'))
    account = 0
    for i in range(number):
        money = int(input('how much?'))
        account = account + money
    print('you have added',account, 'in your account')
    question=input('do you want to transfer the money batches?')
    while question == 'yes':
        question = transfer()


if question == 'transfer':
    transfer()
    

