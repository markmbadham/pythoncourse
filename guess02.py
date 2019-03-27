import random
MIN_RND = 1 
MAX_RND = 10
MAX_GUESSES = 5
rnd = random.randint(MIN_RND,MAX_RND)
print "I have a random number between %d and %d" %(MIN_RND, MAX_RND)

for i in range(MAX_GUESSES):
    guess = int(raw_input("enter your guess: "))
    if guess > rnd:
        print "too high"
    elif guess < rnd:
        print "too low"
    else:
        print "correct"
        break
else: print "you lose"
