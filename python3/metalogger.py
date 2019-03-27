#!/usr/bin/env python3

import logging as l
import traceback as tb
FORMAT = '%(asctime)s:%(levelname)10s:%(message)s'
LEVEL = l.DEBUG
FILENAME = 'metalogger.log'

l.basicConfig(format=FORMAT,filename=FILENAME, level=LEVEL)

def log(fn):
    def inner(*args,**kwargs):
        l.debug("executing %s" % fn.__qualname__)
        try:
            return fn(*args,**kwargs)
        except:
            for line in tb.format_stack():
                l.error(line)
    return inner    

class MetaLogger(type):
    def __new__(cls,name,bases,dct):
        for attribute in dct:
            if callable(dct[attribute]):
                dct[attribute] = log(dct[attribute])
        return super(MetaLogger,cls).__new__(cls,name,bases,dct)

import re
class Config(object,metaclass=MetaLogger):
    FILENAME = 'config.text'
    def __init__(self,filename = 'onfig.text'):
        self.filename = filename
        self.read_config()

    def read_config(self):
        config = open(self.filename)
        for line in  config:
            match=re.search('\s*(.*?)\s*=\s*(.*)',line)
            if match:
                self.__dict__[match.group(1)] = match.group(2)
        config.close()

    def getport(self):
        return self.port
    
    def write(self):
        config = open(self.filename,'w')
        for key in self.__dict__:
            if key != "filename":
                config.write("%s = %s\n" % (key,self.__dict__[key]))
        config.close()

    def display(self):
        for key in self.__dict__:
            print(key,self.__dict__[key])

if __name__ == "__main__":
    conf = Config()
    conf.display()
    conf.port = 10000 
    conf.write()
    print(conf.getport())
    print(Config.__dict__)
