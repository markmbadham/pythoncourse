#!/home/mark/anaconda3/bin/python

import tkinter as tk, sys,math

class GUI(tk.Tk):
    def button_fn(self):
        for key in self.entries:
            print(key, self.entries[key].get())

    def __init__(self,*titles):
        tk.Tk.__init__(self)
        self.buttons = {}
        self.entries = {}
        self.rows = 0
        for title in titles:
            self.add_row(title)
        button = tk.Button(text='print',command=self.button_fn)
        button.grid(row=self.rows+1,column=1,columnspan=2)
        self.mainloop()
                
    def add_row(self,title):
        self.rows +=1
        label = tk.Label(text=title)
        label.grid(column=1, row=self.rows)
        entry = tk.Entry()
        entry.grid(column=2, row=self.rows)
        self.entries[title] = entry

if __name__ == "__main__": GUI('name','surname','age')
