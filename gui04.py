from gui02 import *
from config1 import *

class ConfigGui(BasicGui):

    def button_action(self):
        for key in self.entries:
            self.config.config[key] = self.entries.get()
        self.config.write_file()

    def setup(self): 
        self.config = Config()
        for key in self.config.config:
            self.add_row(key)
            self.entries[key].insert(0,self.config.config[key])
        
        self.button = tk.Button(text='save', command=self.button_action)
        self.button.grid(column=2, row=self.rows+1)



if __name__ == '__main__':
    ConfigGui()
