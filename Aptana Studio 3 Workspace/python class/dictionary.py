'''
Created on 01 Sep 2014

@author: mark
'''

person_dict = {
    'Name': 'Fred',
    'Surname':'Bloggs',
    'Age':10}


for key in person_dict: print key, person_dict[key]

print person_dict.get('name', 'noname')

def square(x):
    return x**2

sq = lambda x: x**2

print sq(2)

s2 = 10
def test_scope():
    global s2
    s2+=1
    print s2
    
test_scope()