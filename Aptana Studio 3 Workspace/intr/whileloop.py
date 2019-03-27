'''
Created on 8 May 2018

@author: mark
'''
n = 0

while n<10:
    
    print n,
    n += 1
#jump to while


print "done"

while True:
    answer = raw_input("Enter Something")
    if answer == 'quit': 
        break
    print "you said " + answer.upper()
