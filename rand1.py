#!/usr/bin/env python3
from random import randint
MIN = 1
MAX = 10
rnd = randint(MIN,MAX)
print("I have a number between %s and %s" % (MIN,MAX))
print(rnd)
guess = int(input("Enter your guess: "))
print(guess)

