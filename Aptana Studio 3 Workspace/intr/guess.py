'''
Created on 8 May 2018

@author: mark
'''
import random

print "this is a guessing game"

min_rnd = int(raw_input('enter the min number'))
max_rnd = int(raw_input('enter the max number'))

rnd = random.randint(min_rnd, max_rnd)
print "i have a number between %d and %d" % (min_rnd, max_rnd)
gueses = ('first', 'second', 'third', 'fourth', 'fifth')
for turn in gueses:
    guess = int(raw_input("Enter your %s guess" % turn))
    
    if guess == rnd:
        print "correct"
        break
    elif guess > rnd:
        print "too high"
    else:
        print "too low"
else: print "sorry you lose"