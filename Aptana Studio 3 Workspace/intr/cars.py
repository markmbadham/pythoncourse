'''
Created on 9 May 2018

@author: mark
'''

class Car(object):
    '''
    classdocs
    '''

    def __init__(self, reg=''):
        '''
        Constructor
        '''
        self.speed = 0
        self.reg = reg
        
    def accelerate(self):
        self.speed += 1
    
    def brake(self):
        self.speed -= 1

ferrari = Car('CA2000')
ferrari.accelerate()
Car.accelerate(ferrari)
ferrari.accelerate()
print ferrari.speed
ferrari.brake()
print ferrari.speed
