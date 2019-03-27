'''
Created on 01 Sep 2014

@author: mark
'''
import random
import matplotlib.pyplot as mp
count = {}
for i in range (1000):
    rnd = random.randint(1,10)
    count[rnd] = count.get(rnd,0)+1
    
print count
#mp.plot(count.keys(),count.values())
#mp.show()

count2 = [0]*11
for i in range (1000):
    rnd = random.randint(1,10)
    count2[rnd] +=1
print count2
mp.plot(range(1,11),count2[1:])
mp.show()