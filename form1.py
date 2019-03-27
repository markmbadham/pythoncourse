import tkinter as tk

class Form(tk.Tk):
    def __init__(self, titles, buttons):
        super().__init__()
        self.titles = titles
        self.button_titles = buttons
        self.buttons = {}
        self.entries = {}
        self.frame = tk.Frame()
        print(self.frame)
        self.row = 0
        self.button_col = 0
        self.add_row(*titles)
        self.frame.grid(row=self.row+1, column=1, columnspan=2)
        self.add_button(*buttons)
        self.setup()
        self.mainloop()

    def add_row(self, *titles):
        '''
        Adds a label and an entry side by side
        using row to keep track of how many we  
        have added.

        @param titles the text to appear on the
                     label
        '''
        row = self.row
        for title in titles:
            row += 1
            label = tk.Label(text=title)
            label.grid(row=row, column=1)
            entry = tk.Entry()
            entry.grid(row=row, column=2)
            self.entries[title] = entry
        self.row = row

    def add_button(self, *titles):
        col = self.button_col
        for title in titles:
            col += 1
            button = tk.Button(self.frame, text=title, command=self.button_command)
            button.grid(row=1, column=col)
            self.buttons[title] = button
        self.button_col = col

    def set_button_command(self, button, command):
        self.buttons[button]['command'] = command
        

    def setup(self):
        # self.set_button_command('print', self.button_command)
        pass

    def button_command(self):
        for title, entry in self.entries.items():
            print(title, entry.get())

if __name__ == '__main__':
    #from threading import Thread
    from multiprocessing import Process
    t1 = Process(
        target=Form, 
        args=(['name', 'surname', 'age'],['print'])
    )
    t1.start()
    t2 = Process(
        target=Form,
        kwargs={'titles':['height', 'width', 'depth'], 'buttons':['press']}
    )
    t2.start()
    Process.join(t1)
    Process.join(t2)
    print("done")