#!/usr/bin/env python3
import sys

print(sys.argv)

if len(sys.argv) > 1:
   num = sys.argv[1]
else:
   num = input('enter something')

if num.isdigit():
   print('digits')
elif num.isalpha():
   print('letters')
elif num.isalnum():
   print('letters and digits')
else:
   print("I don't know what this is")
