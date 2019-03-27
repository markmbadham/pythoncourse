#!/usr/bin/env python
import re
class Config(object):
    def __init__(self,filename = 'config.text'):
        self.filename = filename
        self.read_config()

    def read_config(self):
        config = open(self.filename)
        for line in  config:
            match=re.search('\s*(.*?)\s*=\s*(.*)',line)
            if match:
                self.__dict__[match.group(1)] = match.group(2)
        config.close()
    
    def write(self):
        config = open(self.filename,'w')
        for key in self.__dict__:
            if key != "filename":
                config.write("%s = %s\n" % (key,self.__dict__[key]))
        config.close()

    def display(self):
        for key in self.__dict__:
            print key,self.__dict__[key]

if __name__ == "__main__":
    conf = Config()
    conf.display()
    conf.port = 10000 
    conf.write()
