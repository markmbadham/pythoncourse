#!/usr/bin/env python

import sys
print len(sys.argv)
print sys.argv
if len(sys.argv) > 1: 
    arg = sys.argv[1]
else:
    arg = raw_input('what do you want to do: start, stop or restart: ')

if arg == "start":
    print "Starting ..."
elif arg == "stop":
    print "Stopping ..."
elif arg == "restart":
    print "Stopping ..."
    print "Starting ..."
else:
    print "Usage: stop | start | restart"
