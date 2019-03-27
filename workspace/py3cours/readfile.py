'''
Created on 17 Aug 2017

@author: mark
'''
try:
    f = open('test.log')
    print(f.read())
finally:
    f.close()

with open('test.log') as f:
    print(f.read())

