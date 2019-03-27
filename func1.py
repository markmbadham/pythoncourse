import os
def dircmp(file1, file2):
    isdir1 = os.path.isdir(file1)
    isdir2 =  os.path.isdir(file2)
    if isdir1 and isdir2 or not isdir1 and not isdir2:
        return cmp(file1, file2)
    elif isdir1:
        return 1 
    elif isdir2:
        return -1 

def lister(dir, indent=0):
    files =  os.listdir(dir)  
    files.sort(cmp=dircmp)
    for filename in files:
        path = dir + '/' + filename
        print '  '*indent + filename,
        if os.path.isdir(path): 
           print '/'
           lister(path, indent+1) 
        else: print
lister('.')

files = os.listdir('.')
dirs = filter(lambda x : os.path.isdir(x), files)

def greeter(name):
    return 'hello %s' % name

def make_double(x):
    return x*2

def fact(x):
    ans = 1
    for i in range(1,x+1):
        ans *= i
    return ans


