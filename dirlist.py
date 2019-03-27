import os
def dirlist(path, indent=0):
    print '  '*indent,path
    if os.path.isdir(path):
        print '  '*indent,'-'*len(path)
        os.chdir(path)
        for filename in os.listdir('.'):
            dirlist(filename,indent+1)
        os.chdir('..')

if __name__ == '__main__':
    dirlist('..')
