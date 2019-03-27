import re
FILENAME = 'config.text'
class Config(object):
    def __init__(self):
        self.config_file = open(FILENAME)
        self.config = {}
        for line in self.config_file:
            match = re.search(r'^\s*(\S+)\s*=\s*(\S+)',line)
            if match: self.config[match.group(1)] = match.group(2)
        self.config_file.close()

    def show(self):
        print(self.config)

    def set(self,key,val):
        self.config[key] = val

    def get(self,key):
        return self.config[key]

    def write(self):
        config_file = open(FILENAME, 'w')
        for key in self.config:
            config_file.write('%s = %s\n' % (key, self.config[key]))

        config_file.close()
        
class Config2(Config):
    def get_file(self):
        print(open(FILENAME).read())
        
    def show(self):
        print(self.config)

if __name__ == '__main__':
    config = Config()
    config.show()
    config.set('host','10.0.0.2')        