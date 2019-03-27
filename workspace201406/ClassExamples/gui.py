'''
Created on 12 Jun 2014

@author: mark
'''
import Tkinter as tk
import sys

class BasicGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entries = {}
        self.labels = {}
        self.rows = 0
        self.setup()
        self.mainloop()
        
    def add_row(self,label):
        self.rows += 1
        lab = tk.Label(text=label)
        entry = tk.Entry()
        lab.grid(row=self.rows,column=1)
        entry.grid(row=self.rows,column=2)
        self.entries[label] = entry
        self.labels[label] = lab
    
    def button_command(self):
        for key in self.entries:
            print key, self.entries[key].get()
    
    def setup(self):
        for label in "Name Surname Age".split(" "):
            self.add_row(label)
        print1 = tk.Button(text="print", command=self.button_command)
        print1.grid(row=self.rows+1,column=1,columnspan=2)
         
if __name__ == "__main__": 
    BasicGUI()