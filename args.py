#!/usr/bin/env python3
'''Helo'''
import sys
if len(sys.argv) < 2:
    arg = input("enter stop|start|restart: ")
else:
    arg = sys.argv[1]
if arg == 'start':
    print("starting")
elif arg == 'stop':
    print("stopping")
elif arg == 'restart':
    print("stopping")
    print("starting")
else:
    print("usage: stops|start|restart")

