import tkinter as tk
import logging as log
from gui02 import Form
from dbtest import UserDB
class DBForm(Form):
    
    def button_action(self):
        log.info('button pressed')
        kwargs =  {key:int(val.get()) if key == 'id' else val.get() 
                    for key,val in self.entries.items()}
        self.user.addrow(**kwargs)

    def setup(self):
        self.user = UserDB()
        for title in map(lambda x:x[1],self.user.getcols()):
            self.add_row(title)
        self.button = tk.Button(text='print', command=self.button_action)
        self.button.grid(column=2, row=self.rows+1)

if __name__ == '__main__':
    DBForm()
