email[-1]
len(email)
email[3:10]
email[:10]
email[11:]
email[::-1]
email[::2]
email[5:15:2]
email
print 'fred.bloggs'
atpos = email.find('@')
print email[:atpos]
print email[:email.find('@')]
import math
dir(math)
math.cos(0.5)
from math import cos
cos(0.5)
math.log10(10)
help(math.erf)
help(math.pow)
help(math.log1p)
help(math.e)
math.e
math.pi
dir(math)
print dir(math)
import random
dir(random)
help(random.random)
help(random.randint)
help(random.shuffle)
print random.random()
print random.randint()
print random.randint(1,10)
print random.randint(1,10)
print random.randint(1,10)
print random.randint(1,10)
print random.randint(1,10)
print random.randint(1,10)
help(random.sample)
import random as rnd
rnd.random()
rnd.randint()
rnd.randint(1,10)
from random import randint
randint(1,10)
guess = randint(1,10)
print guess
if True: print "yes"
print 'a'
if True: print "yes"
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import selenium
import sel
from selenium import webdriver
brower = webdriver.Firefox()
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
range(5)
list(range(5))
':'.join(range(5))
':'.join(map(str,range(5)))
list(map(str,range(5)))
list(map(tuple,range(5)))
list(map(type,range(5)))
list(map(lamba x:x**2,range(5)))
list(map(lambda x:x**2,range(5)))
list(map(lambda x:x**2,range(5)))
list(filter(lambda x:x%2==0,range(15)))
[x**2 for x in range(10)]
(x**2 for x in range(10))
list(x**2 for x in range(10))
for i in (x**2 for x in range(10)):
    print(i)
    
o = (x**2 for x in range(10))
o._next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
{chr(x+64):chr(x+90) for x in range(26)}
{chr(x+65):chr(x+90) for x in range(26)}
{chr(x+64):chr(x+90) for x in range(26)}
{chr(x+64):chr(x+80) for x in range(26)}
{chr(x+64):chr(x+90) for x in range(26)}
{chr(x+64):chr(x+90) for x in range(10)}
{chr(x+64):chr(x+95) for x in range(10)}
{chr(x+64):chr(x+96) for x in range(10)}
{chr(x+64):chr(x+97) for x in range(10)}
{chr(x+64):chr(x+96) for x in range(10)}
{chr(x+65):chr(x+96) for x in range(10)}
{chr(x+65):chr(x+97) for x in range(10)}
{chr(x+65):chr(x+97) for x in range(10)}
d = {chr(x+65):chr(x+97) for x in range(10)}
d['A']
from closure import updown
o = updown(5)
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o.__next__()
o = updown(5)
for x in o:
    print(x, end='')
from closure import updown
o = updown(5)
o.__next__()
o.__next__()
o.__next__()
for x in o:
    print(x, end='')
import math
dir(math)
math.pi
from math import cos
cos(0)
__main__.cos
cos
math.sin
import closure as cs
cs.updown(n)
cs.updown(5)
import sys
sys.path
sys.modules
import loops
loops.tree(5)
print(loops.tree(5))
class C: 
    pass
o = C
o = C()
o.__dict__
1/0
int('a')
isinstance(ValueError,Exception)
raise ValueError('message')
try:
    1/0
except ZeroDivisionError:
    print('cannot divide by zero')
assert False, 'message'
raise ValueError('message')
class DufussError(Exception): pass
raise DufussError('message')
class DufussError(Exception): pass
raise DufussError('message')
class DufussError(Exception):
    pass
raise DufussError('message')
number = int(input('enter an int'))
1
number
number = int(input('enter an int'))
a
import logging as log
help(log.basicConfig())
help(log.basicConfig)
q
log.error('Error')
log.basicConfig(filename='test.log')
log.error('Error')
help(log)
print('%s %s %s' % (1,2,3))
print('%(a)s %(b)s %(c)s' % {'a':1,'b':2,'c':3})
import os
os.path.exists('test.log')
os.path.exists('.')
os.path.abspath('.')
os.chdir('Documents/course/python')
os.path.abspath('.')
os.path.exists('hello.py')
os.path.isfile('hello.py')
os.path.isfile('.')
os.path.isdir('.')
os.access('hello.py',os.R_OK)
os.access('hello.py',os.W_OK)
os.access('/home',os.W_OK)
dir(os)
help(os.listdir)
os.listdir('.')
for filename in os.listdir('.'):
    print(filename)
f = open('test.log')
f = open('/home/mark/Documents/course/python/server.log')
f.read()
