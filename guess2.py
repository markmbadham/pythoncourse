#!/usr/bin/env python
from random import randint

max_rnd = 10
min_rnd = 1
rnd = randint(min_rnd,max_rnd)
print "I have a random number between %d and %d" % (min_rnd,max_rnd)
for i in range(5):
    while True:
        try:
            guess = int(raw_input('Enter your guess: '))
        except ValueError:
            print "not a number"
        else: break   

    if guess < rnd: 
        print "Too Low"
    elif guess > rnd: 
        print "Too High"
    else : 
        print "correct"
        break
else:
    print "You loose the answer is %d" % rnd
raw_input()
