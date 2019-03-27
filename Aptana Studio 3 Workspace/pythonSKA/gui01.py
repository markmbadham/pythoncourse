'''
Created on 16 May 2018

@author: mark
'''
import Tkinter as tk

FILENAME = '../../config.text'

class GUI1(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.text = tk.Text()
        self.text.grid(row=2, column=1, columnspan=3)
        open_button = tk.Button(text='open', command=self.button_open)
        open_button.grid(row=1, column=1)
        write_button = tk.Button(text='save', command=self.button_write)
        write_button.grid(row=1, column=2)
        self.file_name_entry = tk.Entry()
        self.file_name_entry.grid(row=1, column=3)
    
    def button_open(self):
        filename = self.file_name_entry.get()
        with open(filename if filename else FILENAME) as f:
            self.text.insert(0.0, f.read(4096))
    
    def button_write(self):
        filename = self.file_name_entry.get()
        with open(filename if filename else FILENAME, 'w') as f:
            f.write(self.text.get(0.0, tk.END))

#button['command'] = button_press

if __name__ == '__main__':
    win = GUI1()
    win.mainloop()