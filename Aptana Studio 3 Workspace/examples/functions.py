'''
Created on 21 Oct 2014

@author: mark
'''
def greeter(name='',surname=''):
    return "hello %s %s" % (name,surname)



def test_args(*args,**kwargs):
    for a in args:
        print a
    for key in kwargs:
        print key, kwargs[key]


#test_args(1,2,3,4,a=10,n=20,c=30)

def interest(principle, rate, nper):
    return principle(1+rate)**nper

def fact(x):
    out =1
    for i in range(1,x+1):
        out*=i
    return out
        

def sum(*args):
    out=0
    for a in args:
        out +=a
    return out

#print sum(1,2,3,4)        

x = [5]
def double(x):
    x += x
    print x
    
double(x)
print x

def make_double(fn):
    def inner(*args,**kwargs):
        return 2*fn(*args,**kwargs)
    return inner

@make_double
def square(x):
    return x**2

#square = make_double(square)












