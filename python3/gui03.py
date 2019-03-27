import tkinter as tk
import sys

class Form(tk.Tk):

    def __init__(self, *args):
        tk.Tk.__init__(self)
        self.entries = {}
        self.rows, self.cols = 1,1
        self.setup(*args)

    def button_action(self):
        for key in self.entries:
            self.text.insert(tk.END,"%s %s\n" % (key, self.entries[key].get()))

    def add_row(self,title):
        self.rows +=1
        label = tk.Label(text=title)
        label.grid(column=1, row=self.rows)
        entry = tk.Entry()
        entry.grid(column=2, row=self.rows)
        self.entries[title] = entry

    def setup(self, *args):
        for title in args: self.add_row(title)
        button = tk.Button(text='press', command = self.button_action)
        button.grid(row=self.rows+1, column=1) 
        self.text = tk.Text()
        self.text.grid(row=self.rows+2, column=1, columnspan=2)
        self.mainloop()


if __name__ == '__main__':
    Form('name','surname','age')
