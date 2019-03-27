'''
Created on 15 Aug 2017

@author: mark
'''
def greeter(name, surname = ''):
    return 'hello {} {}'.format(name, surname)

def square(x):
    return x**2


import math
def square2(x):
    return math.pow(x,2)

def interest(principle, rate, nper):
    return principle * (1+rate)**nper



def tree(n):
    output = []
    for i in range(1,n+1):
        output.append(('* '*i).center(2*n))
    return '\n'.join(output)

def testargs(*args,**kwargs):
    print(args,kwargs)


    
def avg(*args):
    return sum(args)/len(args)




if __name__ == '__main__':
    print(square(3))
    testargs(1,2,3,A='a',B='b')
    print(avg(1,2,3,4,5))
    '''
    print(interest(1000,0.012,36))
    
    rate = float(input('what is the percent interest '))/100
    principle = float(input('What is the principle '))
    nper = int(input('how many periods '))
    
    print(interest(principle, rate, nper))
    '''




