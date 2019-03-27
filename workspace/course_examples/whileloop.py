'''
Created on 08 Nov 2016

@author: mark
'''
x = 0
while x < 10:
    print x
    x += 1

#line = ""
#while line != 'quit':
while True:
    line = raw_input("Enter something:")
    print line.upper()
    if line == 'quit': break
print "done"



