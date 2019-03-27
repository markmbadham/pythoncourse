#! /opt/anaconda/bin/python



import random

guess = int(raw_input('Please guess a number between 1 and 10): '))
rnd = random.randint(1,10)
if guess > rnd : guess = int(raw_input('You are too high, please guess again: '))
elif guess < rnd : guess = int(raw_input('You are too low, please guess again: '))
elif guess == rnd : print "You WIN!!!"
while guess != rnd:
    if guess > rnd : guess = int(raw_input('You are still too high, please guess again: '))
    elif guess < rnd : guess = int(raw_input('You are still too low, please guess again: '))
    if guess == rnd : print "You WIN!!!"
