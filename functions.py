#!/usr/bin/env python

def greeter(name="",surname=""):
    return  "hello %s %s" % (name, surname)


'''
print greeter()
print greeter("fred")
o
print greeter("fred","basset")
'''
def sum(*args):
    sum=0
    for arg in args: sum += arg
    return sum

def tree(n):
    out = ''
    for i in range(1,n+1):
        out += ('* '*i).center(n*2) + '\n'
    return out

def fact(n):
    out = 1
    #for i in range(1,n+1):
    for i in range(n,0,-1):
        out *= i
    return out

def factr(n):
    return 1 if n<=1 else n*factr(n-1)

#tree(int(sys.argv[1]))
#tree(10)
def interest(principle,rate,nper):
    return principle*(1+rate)**nper

if __name__ == '__main__':
    print fact(6)

