#!/usr/bin/env python3
'''
This is a module for reusable functions
@version 1
@author mark

'''

def greeter(name="",surname=""):
    '''
    Function returns a greeting string
    '''
    return  "hello %s %s" % (name, surname)


def square(x):
    ''' 
    returns the square of x
    >>> square(2)
    4
    >>> list(map(square, range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    '''
    return x**2

def sum(*args):
    '''
    >>> sum(1,2,3,4)
    10
    '''
    out = 0
    for arg in args: out += arg
    return out


def _test():
    import doctest
    doctest.testmod(1)

def tree(n):
    for i in range(1,n+1):
        print(('* '*i).center(n*2))

    
def interest(principle,rate,nper):
    return principle*(1+rate)**nper


if __name__ == "__main__":
    #print(square(2))
    _test()







