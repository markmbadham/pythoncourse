#! /usr/bin/env python

import os

def listdir(dir,indent=0):
    print('  '*indent,dir)
    if os.path.isdir(dir):
        os.chdir(dir)
        for filename in os.listdir('.'):
             listdir(filename,indent+1)
        os.chdir('..')

listdir('.')
