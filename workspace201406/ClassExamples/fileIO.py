'''
Created on 11 Jun 2014

@author: mark
'''
import os, re

def lister(path,indent=0):
    '''lister
       lists a directory recursively
       with an output similar to ls
       '''
    if os.path.isdir(path):
        os.chdir(path)
        for file in os.listdir('.'):
            print '   '*indent,file
            lister(file,indent+1)
        os.chdir('..')

def lister2(path):
    '''lister2
    recusive directory lister with an output sililar to find'''
    
    if os.path.isdir(path):
        abspath = os.path.abspath(path)
        for file in os.listdir(abspath):
            absfile = abspath+os.sep+file
            print absfile
            lister2(absfile)
        
def readfile(filename):
    for line in open(filename):
        print line,
import re
def showval(filename,search):
    data = open(filename).read()
    match = re.search("^"+search+r"\s*=\s*(\S+)", data,re.M)
    if match : print match.group(1)


class config(object):
    def __init__(self,filename='/home/mark/Documents/course/python/config.text'):
        self.filename=filename
        self.read_config()
    
    def read_config(self):
        for line in open(self.filename):
            match = re.search("^\s*(\S+)\s*=\s*(\S+)", line)
            if match : self.__dict__[match.group(1)] = match.group(2)
        return config
    
    @staticmethod
    def dict_string(d,exclude=[]):
        out = ''
        for key in d: 
            if not key in exclude: out += "%s = %s\n" % (key,d[key])
        return out
    
     
    def write_config(self):
            f = open(self.filename,'w')
            f.write(self.dict_string(self.__dict__),['filename'])
            f.close()
                


if __name__ == "__main__":
    print read_config('/home/mark/Documents/course/python/config.text')