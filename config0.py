#!/usr/bin/env python3
FILENAME = 'config.text'

class Config(object):
    def __init__(self,filename=FILENAME):
        self.file_name = filename
        self.readfile()

    def readfile(self):
        f = open(self.file_name)
        self._config = {}
        for line in f:
            try:
                key,val = line.split('=')
            except ValueError:
                pass
            self._config[key.strip()] = val.strip()
        f.close()

    def get_port(self):
        return self._config['port']

    def save_file(self):
        f = open(self.file_name,'w')
        f.write(self.__str__())
        f.close()

    def __getattr__(self,name):
       if name in self._config:
           return  self.__dict__['_config'][name]
       else:
           raise AttributeError("'Config object has no attribute '%s'" % name)

    def __setattr__(self, name, value):
        if name in self._config:
           self.__dict__['_config'][name] = value 
        else: 
            object.__setattr__(self,name,value)

    def __str__(self):
        out = ''
        for key,val in self._config.items():
            out += '%s = %s\n' % (key,val)
        return out

if __name__ == "__main__":
    conf = Config()
    print(conf)
    conf.port = 4000
    conf.save_file()
    print(conf.dbname)

