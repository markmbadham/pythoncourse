'''
Created on 17 Aug 2017

@author: mark
'''
import os

def dirlist(path, indent=0):
    print('   '*indent,path)
    if os.path.isdir(path):
        os.chdir(path)
        for filename in os.listdir('.'):
            dirlist(filename, indent+1)
        os.chdir('..')

if __name__ == '__main__':
    dirlist('..')
        
        