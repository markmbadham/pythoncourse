'''
Created on 09 Mar 2016

@author: mark
'''
from paramiko.agent import Agent

class Person(object):
    '''
    classdocs
    '''


    def __init__(self, name="", age=0):
        '''
        Constructor
        '''
        self.name = name
        self.age = age
        
    def talk(self):
        return " Hello my name is %s" % self.name
    
if __name__ == "__main__":
    o =  Person(name="fred", age=100)
    print(o.talk())
    ''.