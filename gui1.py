import Tkinter as tk
class FileEditor(tk.Tk):
    def __init__(self, filename='config.text'):
        tk.Tk.__init__(self)
        self.rows = 0
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.text = tk.Text()
        self.filename = filename

    def add_entry(self,label):
        self.rows += 1
        self.entries[label] = tk.Entry()
        self.entries[label].grid(row = self.rows, column = 2)
        self.labels[label] = tk.Label(text = label)
        self.labels[label].grid(row = self.rows, column = 1)

    def open_file(self):
        self.text.insert(0.0, open(self.entries['file'].get()).read())

    def write_file(self):
        f = open(self.entries['file'].get())
        f.write(self.text.get(1.0,tk.END))
        f.close()

    def setup(self):
        self.rows +=1
        open_button = tk.Button(text='open', command = self.open_file)
        open_button.grid(row = self.rows, column =1)
        close_button = tk.Button(text='close', command = self.write_file)
        close_button.grid(row = self.rows, column =2)
        self.add_entry('file')
        self.entries['file'].insert(0,self.filename)
        self.rows +=1
        self.text.grid(row=self.rows, column=1, columnspan = 2)

if __name__ == '__main__':        
    win = FileEditor()
    win.setup()
    win.mainloop()
