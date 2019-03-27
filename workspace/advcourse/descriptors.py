'''
Created on 29 Apr 2017

@author: mark
'''

class Desc(object):
    '''
    classdocs
    '''


    def __init__(self, x):
        '''
        Constructor
        '''
        self.x = x
        
    def __set__(self,x,val):
        print 'setting %s' % x
        self.x = val
    
    def __get__(self, obj,obtype):
        print 'getting', obj, obtype
        return self.x 

class TestDesc(object):
    a= Desc(5)
    b = Desc(4)

c = TestDesc()
print c.a  
print c.b
c.a = 10
