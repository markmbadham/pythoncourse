#!/usr/bin/env python
import sys
print sys.argv
if len(sys.argv) < 2:
    age = int(raw_input('Enter your age: '))
else:
    age = int(sys.argv[1])

if age < 1 and age >=0:
    print 'baby'
elif age < 10:
    print 'child'
elif age < 13:
    print 'pre-teen'
elif age < 20:
    print 'teen'
elif age >= 20 and age < 120:
    print 'adult'
else :
    print 'incorrect age'
