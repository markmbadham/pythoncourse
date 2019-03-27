#!/usr/bin/env python3

import logging as l
import traceback as tb
FORMAT = '%(asctime)s:%(levelname)10s:%(message)s'
LEVEL = l.DEBUG
FILENAME = 'logging.log'

l.basicConfig(format=FORMAT,filename=FILENAME, level=LEVEL)

def log(fn):
    def inner(*args,**kwargs):
        l.debug("executing %s" % fn.__repr__())
        try:
            return fn(*args,**kwargs)
        except:
            for line in tb.format_stack():
                l.error(line)
    return inner    
