'''
Created on 18 Jul 2014

@author: mark
'''
import Tkinter as tk
class Form1(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.row=1
        self.labels = {}
        self.entries = {}
    
    def print_entries(self):
        for title in self.entries:
            print title,self.entries[title].get()

    def add_row(self,title):
        self.labels[title] = tk.Label(text=title)
        self.labels[title].grid(row=self.row, column=1)
        self.entries[title] = tk.Entry()
        self.entries[title].grid(row=self.row, column=2)
        self.row +=1
if __name__=='__main__':
    win = Form1()
    for title in ['Name', 'Surname', 'Age']:
        win.add_row(title)
    button = tk.Button(text="Print", command=win.print_entries)
    button.grid(rows=win.row+1,column=1,columnspan=2)         
    win.mainloop()