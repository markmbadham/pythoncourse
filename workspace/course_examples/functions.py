'''
Created on 09 Nov 2016

@author: mark
'''

def greeter(name, surname=''):
    if surname:
        return 'hello %s %s' % (name, surname)
    else: 
        return 'hello %s' % name

#print greeter('fred')

print greeter(surname='fred', name='basset')

def square(x):
    return x**2

#print square(int(raw_input('Enter a number: ')))

def tree(n=4):
    out = ''
    for i in range(1,n+1): 
        out += (i*'* ').center(n*2) + '\n'
    return out


def tree2(n=4):
    out = []
    for i in range(1,n+1):
        out.append((i*'* ').center(n*2))
    return '\n'.join(out)

print tree2(20)

def get_int(prompt='Enter an int '):
    while True:
        myint = raw_input(prompt)
        if myint.isdigit(): break
        else: print "not an int"
    return int(myint)

print get_int()

