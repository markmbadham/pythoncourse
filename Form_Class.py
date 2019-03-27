import tkinter as tk
class Form(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.rows = 0
        self.entries = {}
        self.setup()

    def add_row(self, title):
        label = tk.Label(text=title)
        label.grid(row=self.rows, column=0)
        entry = tk.Entry()
        entry.grid(row=self.rows, column=1)
        self.entries[title] = entry
        self.rows+=1

    def button_action(self):
        for key in self.entries:
            print(key, self.entries[key].get())

    def setup_rows(self, *titles):
        for title in titles:
            self.add_row(title)
    
    def setup(self):
        self.setup_rows('Name','Surname','Age')
        button = tk.Button(text='Print', command=self.button_action)
        button.grid(row=self.rows+1,column=0)
        self.mainloop()

if __name__ == '__main__':
    win = Form()

