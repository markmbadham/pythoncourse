#!/usr/bin/env python3
import os

def listdir(filename,indent=0):
    print('   '*indent,os.path.basename(filename))
    if os.path.isdir(filename):
        curdir = os.path.abspath('.')
        os.chdir(filename)
        for newfile in os.listdir('.'):
            listdir(newfile,indent+1)
        os.chdir(curdir)

def listdir2(filename,indent=0):
    print('   '*indent,os.path.basename(filename))
    filename = os.path.abspath(filename)
    if os.path.isdir(filename):
        for newfile in os.listdir(filename):
            listdir2(filename +'/'+newfile,indent+1)
listdir2('/usr/local')
