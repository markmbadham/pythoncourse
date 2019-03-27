import tkinter as tk
import sys
entries = {}

def button_action():
    for key in entries:
        print(key, entries[key].get())

win = tk.Tk()
rows, cols = 1,1
button = tk.Button(text='press', command = button_action)
button.grid(row=rows, column=cols) 

def add_row(title):
    global rows
    rows +=1
    label = tk.Label(text=title)
    label.grid(column=1, row=rows)
    entry = tk.Entry()
    entry.grid(column=2, row=rows)
    entries[title] = entry

for title in ['name','surname','age']: add_row(title)

text = tk.Text()
text.grid(row=rows+1, column=1, columnspan=2)
win.mainloop()
