'''
Created on 25 May 2017

@author: mark
'''
from time import sleep

def loop_nos():
    print("Starting P1")
    for i in xrange(10):
        sleep(1)
        print (str(i))
        yield

def loop_chars():
    print("Starting P2")
    for j in xrange(65,76):
        sleep(1)
        print(chr(j))
        yield

nos_gen = loop_nos()
chars_gen = loop_chars()

for i in range(10):
    next(nos_gen)
    next(chars_gen)

