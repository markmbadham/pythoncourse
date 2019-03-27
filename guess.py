#!/usr/bin/env python

'''
   Guessing game
   version 0.1
'''

from random import randint

MIN_RAND = 1
MAX_RAND = 10
NO_GUESSES = 5
RANDOM_NO = randint(MIN_RAND, MAX_RAND)

print "I have a number between %s and %s" % (MIN_RAND, MAX_RAND)

for x in range(NO_GUESSES):
    guess = int(raw_input("guess: "))

    if guess > RANDOM_NO:
        print "too high"
    elif guess < RANDOM_NO:
        print "too low"
    else: 
       print "correct"
       break

else: print "you lose, answer is : %s " % RANDOM_NO
