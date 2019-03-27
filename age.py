#!/usr/bin/env python
import sys
if len(sys.argv) > 1:
    age = int(sys.argv[1])
else:
    age = int(raw_input('Enter age: '))

if age<1:
    print "baby"
elif age<13: 
    print "child"
elif age>18: 
    print "adult"
else : 
    print "teenager"

raw_input()
