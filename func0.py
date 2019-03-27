#!/usr/bin/env python3
'''
A cluster of not so useful functions
For the purpose of demonstrating python function syntax
'''

def greeter(name, surname=''):
    #print('hello')
    return 'hello %s how is the %s family' % (name,surname);

def square(x):
    return x**2

def interest(p, r, n):
    '''compound interest = 
    principle times 1+interest rate to 
    the power of the number of periods
    interest(p, r, n) -> comound_interest
    p principle
    r interest rate
    n number of periods
    '''
    return p*(1+r)**n

def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factr(n):
    return 1 if n <= 1 else n * factr(n - 1)

def sum(*args):
    result = 0
    for arg in args:
        result+=arg
    return result


if __name__ == "__main__":
    print(factr(5))
    print (square(2))
    print(greeter('fred'))
    print(interest(1000,.01,36))
    print(fact(5))
    print(sum(1,2,3,4))

