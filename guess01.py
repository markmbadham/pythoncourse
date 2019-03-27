import random
MIN_RND = 1 
MAX_RND = 10
rnd = random.randint(MIN_RND,MAX_RND)
print "I have a random number between %d and %d" %(MIN_RND, MAX_RND)
guess = int(raw_input("enter your guess: "))

if guess > rnd:
    print "too high"
elif guess < rnd:
    print "too low"
else:
    print "correct"

