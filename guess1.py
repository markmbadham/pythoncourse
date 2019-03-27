#!/usr/bin/env python
'''
Guessing game
@version 0.1
@author Mark
'''
from random import randint

MAX_RND = 10
MIN_RND = 1
rnd = randint(MIN_RND,MAX_RND)
print "I have a random number between %d and %d" % (MIN_RND,MAX_RND)

guess = MAX_RND + 1
while(rnd != guess):
    while(True):
        try:
            guess = int(raw_input('Enter your guess: '))
        except ValueError:
            print "must be a number"
        else: break
        finally: print "cool"

    if guess < rnd: 
        print "Too Low"
    elif guess > rnd: 
        print "Too High"
    else : 
        print "correct"

raw_input()
