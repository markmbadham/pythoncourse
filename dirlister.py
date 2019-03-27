import os

def listdir1(path, indent=0):
    print('  '*indent, path)
    if os.path.isdir(path):
        old_path = os.path.abspath('.')
        os.chdir(path)
        for filename in os.listdir('.'):
            listdir1(filename, indent+1)
        os.chdir(old_path)

def listdir2(path):
    print(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            listdir2(path + '/' + filename)

if __name__ == '__main__':
    listdir1('.')