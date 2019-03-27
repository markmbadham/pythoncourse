'''
Created on 16 Aug 2017

@author: mark
'''
def make_double(fn):
    def inner(*args, **kwargs):
        return 2*fn(*args, **kwargs)
    return inner

@make_double
def square(x):
    return x**2
#square = make_double(square)

print(square(3))


cube = lambda x,y=3: x**y

def updown(n):
    for i in range(n): yield i
    for i in range(n,1,-1): yield i





