import tkinter as tk
import logging as log
log.basicConfig(
    filename='gui.log', 
    format='%(asctime)s:%(levelname)10s:%(name)s:%(message)s',
    level=log.DEBUG)

class Form(tk.Tk):
    def __init__(self):
        log.debug('constructor called')
        tk.Tk.__init__(self)  
        self.labels = {}
        self.entries = {}
        self.rows = 0
        self.setup()
        self.mainloop()

    def add_row(self, title):
        log.debug('adding row: %s' % title)
        self.rows += 1
        label = tk.Label(text=title)
        label.grid(row=self.rows, column=1)
        entry = tk.Entry()
        entry.grid(row=self.rows,column=2)
        self.labels[title] = label
        self.entries[title] = entry
    
    def button_action(self):
        log.info('button pressed')
        for key in self.entries:
            print(self.entries[key].get())


    def setup(self):
        for title in ['name','surname','age']:
            self.add_row(title)
        self.button = tk.Button(text='print', command=self.button_action)
        self.button.grid(column=2, row=self.rows+1)

if __name__ == '__main__':
    Form()
