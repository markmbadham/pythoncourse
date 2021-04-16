import tkinter as tk
import logging as log
log.basicConfig(level=log.DEBUG)

class Form(tk.Tk):
    def __init__(self):
        super().__init__()
        self.rows = 0
        self.entries = {}
        self.setup()
        log.debug('set up complete')
        self.mainloop()

    def add_row(self, text):
        log.debug('adding row {}'.format(text))
        label = tk.Label(text=text)
        entry = tk.Entry()
        self.rows += 1
        label.grid(row=self.rows, column=1)
        entry.grid(row=self.rows, column=2)
        self.entries[text] = entry

    def button_command(self):
        for text in self.entries:
            print(text, self.entries[text].get())
    
    def setup_rows(self, *texts):
        for text in texts:
            self.add_row(text)
    
    def add_button(self, text, command):
        button = tk.Button(text=text, command=command)
        self.rows += 1
        button.grid(row=self.rows, columnspan=2, column=1)

    def setup(self):
        self.setup_rows('name', 'surname', 'age')
        self.add_button(print, self.button_command)

if __name__ == '__main__':
    Form()