#!/usr/bin/env python

from random import randint

min = 1
max = 10
random_no = randint(min,max)

print("I have a number between %s and %s" % (min,max))

for x in range(5):
   while True:
       try:
	   guess = int(input("guess: "))
       except ValueError:
	   print("Guess must be a number")
	   continue
       break

   if guess > random_no: print("too high")
   elif guess < random_no: print("too low")
   else: 
      print("correct")
      break
else: print("you lose, answer is : %s " % random_no)
