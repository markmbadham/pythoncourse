'''
Created on 13 Jun 2014

@author: mark
'''
from gui import  BasicGUI
import Tkinter as tk
from userdb import UserDB

class DbForm(BasicGUI):
    '''
    classdocs
    '''

    def button_command(self):
        fields = {}
        for key in self.entries:
            fields[key] = self.entries[key].get()
        self.userdb.add_user(**fields)
    
    def setup(self):
        self.userdb = UserDB()
        for label in self.userdb.getfields():
            self.add_row(label)
        insertbutton = tk.Button(text="insert", command=self.button_command)
        insertbutton.grid(row=self.rows+1,column=1,columnspan=2)
if __name__ == "__main__":
    DbForm()