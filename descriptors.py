#! /usr/bin/env python3

class C(object):
    
    def __init__(self):
        self._x = 0
    
    def __get__(self):
        return self._x
    
    def __set__(self,val):
        self._x = val if val > self._x else self._x 
 
c = C()
c = 10
c = 11
print(c) #gives 11
c = 5
print(c) #still 11
c += 1
print(c) #prints 12
c -= 1
print(c) #still 12
