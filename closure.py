#!/usr/bin/env python3

def make_double(fn):
    def inner(*args,**kwargs):
        return 2*fn(*args,**kwargs)
    return inner

@make_double
def square(x):
    return x**2

#square = make_double(square)

print(square(3))

def power(x,y):
    return x**y

def defaultval(fn,default):
    def inner(x):
        return fn(x,default)
    return inner

cube = defaultval(power,3)

print(cube(2))
