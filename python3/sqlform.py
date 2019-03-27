from gui03 import Form
import tkinter as tk
from useddb import UserDB

class UserForm(Form):
    def button_action(self):
        db = UserDB()
        db.adduser(self.entries['id'].get(),self.entries['username'].get(),self.entries['password'].get())

if __name__ == '__main__':
    UserForm('id','username','password')
