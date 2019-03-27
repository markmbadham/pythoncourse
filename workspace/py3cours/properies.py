'''
Created on 18 Aug 2017

@author: mark
'''
class C(object):
    
    def __init__(self):
        self._x = 0
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,val):
        self._x = val if val > self._x else self._x
        

c = C()
c.x = 10
c.x = 11
print(c.x)
c.x = 5
print(c.x)
c.x += 1
print(c.x)
c.x -= 1
print(c.x)
