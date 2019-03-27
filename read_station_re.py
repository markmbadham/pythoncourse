# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:11:41 2017

@author: mark
"""
import re

def get_val1(key):
    with open('Desktop/station1.txt') as station1:
        for line in station1:
            match = re.search(r'{}\s*=\s*(\w+)'.format(key),line)
            if match:
                return match.group(1)

def get_val2(key):
    content = open('Desktop/station1.txt').read()
    match = re.search(r'^{}\s*=\s*(\w+(\.\d+)?)\s*$'.format(key),
                      content,re.M+re.I)
    if match:
       return match.group(1)



#print('humidity',get_val1('humidity'))
#print(get_val2('wind speed'))

def read_dict1(filename):
    d = {}
    with open(filename) as station1:
        for line in station1:
            match = re.search(r'\s*([^=]+)\s*=\s*(\w+)',
                                 line)
            if match:
              d[match.group(1)] = match.group(2)
    return d

#print(read_dict1('Desktop/station1.txt'))

def read_dict2(filename):
    d = {}
    with open(filename) as station1:
        for line in station1:
            key,val = re.split(r'\s*=\s*', line)
            d[key] = val
    return d

#print(read_dict2('Desktop/station1.txt'))

def read_dict3(filename):
    content = open(filename).read()
    return dict(re.findall(r'^\s*([^=]+)\s*=\s*(.+?)\s*$', 
                           content,re.M))

print(read_dict3('Desktop/station1.txt'))
 