#!/usr/bin/env python3
import os
def dirlist(dirname='.',indent=0):
    print('  '*indent,dirname)
    if os.path.isdir(dirname):
        os.chdir(dirname)
        for filename in os.listdir('.'):
            dirlist(filename, indent+1)
        os.chdir('..')

def dirlist2(dirname='.', indent=0):
    print('  '*indent,dirname)
    if os.path.isdir(dirname):
        for filename in os.listdir(dirname):
            dirlist3(dirname + '/'+ filename, indent+1)

def dirlist3(dirname='.', indent=0):
    print('  '*indent,dirname)
    if os.path.isdir(dirname):
        for filename in os.listdir(dirname):
            dirlist3(os.path.abspath(filename), indent+1)

if __name__ == '__main__':
    dirlist('.')
    dirlist2('/usr/local')
    dirlist3('/usr/local')
