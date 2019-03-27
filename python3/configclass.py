#!/usr/bin/env python3
import re
from logger_class import log
class Config(object):
    @log
    def __init__(self,filename = 'onfig.text'):
        self.filename = filename
        self.read_config()

    @log
    def read_config(self):
        config = open(self.filename)
        for line in  config:
            match=re.search('\s*(.*?)\s*=\s*(.*)',line)
            if match:
                self.__dict__[match.group(1)] = match.group(2)
        config.close()

    @log
    def getport(self):
        return self.port
    
    @log
    def write(self):
        config = open(self.filename,'w')
        for key in self.__dict__:
            if key != "filename":
                config.write("%s = %s\n" % (key,self.__dict__[key]))
        config.close()

    @log
    def display(self):
        for key in self.__dict__:
            print(key,self.__dict__[key])

if __name__ == "__main__":
    conf = Config()
    conf.display()
    conf.port = 10000 
    conf.write()
    print(conf.getport())
