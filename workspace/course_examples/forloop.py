'''
Created on 08 Nov 2016

@author: mark
'''
for x in range(5): 
    line = raw_input("%d>" %x)
    if line.lower() == 'quit':break
else : print "you are not a quitter"
