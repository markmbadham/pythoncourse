#!/usr/bin/env python
import sys
if len(sys.argv)>1:
    age = sys.argv[1]
else:
    age = raw_input('Enter your age : ')
while True:
    try:
        age = int(age)
    except ValueError:
        print "must be an integer"
        age = raw_input('Enter your age : ')
    else:
        break

if age < 1: print 'baby'
elif age < 10: print 'child'
elif age < 13: print 'preteen'
elif age < 20: print 'teen'
else: print 'adult'

