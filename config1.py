import re
class Config(object):
    def __init__(self, filename='config.text'):
       self.filename = filename
       self.readconfig()

    def readconfig(self):
        f = open(self.filename)
        self.config = {}
        regex = r'^\s*(\S+)\s*=\s*(\S+)\s*$'
        for match in re.finditer(regex, f.read(),re.M):
            self.config[match.group(1)] = match.group(2)

    def get_val(self, key):
        return self.config[key]

    def set_val(self, key, val):
        self.config[val] = val

    def write_config(self):
        f = open(self.filename, 'w')
        for key in self.config:
            f.write('%s = %s\n' % (key, self.config[key]))
        f.close()

    def __del__(self):
        self.write_config()

if __name__ == '__main__':
    my_config = Config(filename='config.text')
    print(my_config.config)
    print(my_config.get_val('port'))
    my_config.set_val('port', 4333)
    print(my_config.config)
    #my_config.write_config()

