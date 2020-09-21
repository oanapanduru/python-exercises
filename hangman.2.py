# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:17:19 2020

@author: oanap
"""
given_word = 'elefant'
guesses = 6
guessed_word = ''
def replace_at_index(string, position, new):
    string = string[:position]+ new + string[position+1:]
    return string
for i in range(len(given_word)):
    guessed_word = guessed_word + '_'
print(guessed_word)
while guesses > 0:
    given_letters = str(input('give me one letter:'))
    lenght = len(given_letters)
    if lenght != 1:
        print('wrong input')
        continue
    if given_letters in given_word:
        print('yes')
        for i in range(len(given_word)):
            if given_word[i] == given_letters:
                guessed_word = replace_at_index(guessed_word, i, given_letters)
                print(guessed_word)
        if given_word == guessed_word:
            print('great job!')
            break
    else:
        print('not in word!')
        guesses -= 1
    