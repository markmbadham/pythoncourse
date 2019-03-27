'''
Created on 10 Jun 2014

@author: mark
'''

def test_args(*args,**kwargs):
    for arg in args: print arg
    for key in kwargs: print key, kwargs[key] 
    
def make_double(fn):
    def inner(*args,**kwargs):
        return 2*fn(*args,**kwargs)
    return inner

@make_double
def square(x):
    return x**2
#square = make_double(square)

def fact(x):
    result = 1
    for n in range(1,x+1):
        result *= n
    return result 
fact = make_double(fact)

def updown(n):
    for x in xrange(n): yield x
    for x in xrange(n,1,-1): yield x

def factr(x):
    return 1 if x<=1 else x * factr(x-1)

def sum(*args):
    result = 0
    for arg in args: result += arg # result = result + arg
    return result

if __name__ == "__main__":
    test_args(1,2,3,4,name='fred',age=10)
