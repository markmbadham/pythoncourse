import os
def dirlist(dirname, indent=0):
    print('   '*indent + dirname)
    if os.path.isdir(dirname):
        os.chdir(dirname)
        for  filename in os.listdir('.'):
            dirlist(filename, indent+1)
        os.chdir('..')

if __name__ == '__main__':
    dirlist('/usr/share')
