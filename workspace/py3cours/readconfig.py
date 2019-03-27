'''
Created on 17 Aug 2017

@author: mark
'''
FILENAME ='/home/mark/Documents/course/python/config.text' 
def get_val(key):
    with open(FILENAME) as f:
        for line in f:
            if line.startswith(key):
                return line.split('=')[1].strip()

def read_dict(filename=FILENAME):
    d = {}
    with open(filename) as f:
        for line in f:
            if '=' in line:
                key,val = line.split('=')
                d[key.strip()] = val.strip()
    return d

def write_dict(filename,d):
    with open(filename,'w') as f:
        for item in d.items():
            f.write("%s = %s\n" % item)

class Config(object):
    def __init__(self, filename=FILENAME):
        self.filename = filename
        self.config = read_dict(filename)
    
    def get_val(self,key):
        return self.config[key]
    
    def set_val(self,key,val):
        self.config[key] = val
        
    def save(self):
        write_dict(self.filename, self.config)

if __name__ == '__main__':
    print(Config().get_val('port'))
