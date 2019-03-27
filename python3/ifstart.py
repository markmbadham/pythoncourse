#!/usr/bin/env python
import sys
if len(sys.argv) > 1:
   ans = sys.argv[1]
else: 
   ans = input("What do you want to do? ")

if ans.lower() == "start":
    print("starting")
elif  ans.lower() == "stop":
    print("stopping")
elif  ans.lower() == "restart":
    print("stopping")
    print("starting")
else :
    print("enter stop or start or restart")

input("press enter")
