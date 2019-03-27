FILENAME = 'config.text'
import re
class Config(object):

    def __init__(self,filename=FILENAME):
        self.config = {}
        self.filename = filename
        self.get_config()

    def get_config(self):
        config = {}
        for line in open(self.filename):
            match = re.search(r'^\s*(\w+)\s*=\s*(\w+)\s*$',line)
            if match:
                key, val = match.groups()
                config[key] = val
        self.config = config

    def __getattr__(self,attr):
        if attr != 'config' and attr in self.config:
            return self.config.get(attr)
        else:
            raise AttributeError,\
                  "%s has no attribute %s" %(self,attr)

    def __setattr__(self,attr,val):
        if attr != 'config' and attr in self.config:
            self.config[attr] = val
        else:
            super(Config, self).__setattr__(attr, val)

    def write_config(self, filename=None):
        filename = filename if filename else self.filename
        f = open(filename, 'w')
        for item in self.config.items():
            f.write('%s = %s\n' % item)
        f.close()

if __name__ == '__main__':
    config = Config()
    print config.config 
    print config.port 
    config.port = 10001
    print config.port 
    config.write_config()
    print open(FILENAME).read()

