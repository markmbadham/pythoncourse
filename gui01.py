
import tkinter as tk
import sys
win = tk.Tk()
buttons = {}
col = 1
row = 1
labels = {}
entries= {}
for text in ('Name','Surname','Age'):
    label = tk.Label(text=text)
    label.grid(row=row,column=1)
    labels[text] = label
    entry = tk.Entry()
    entry.grid(row=row,column=2)
    entries[text] = entry
    row+=1

def list_entry():
    for key in entries:
        print(key + ' ' + entries[key].get())

list_button = tk.Button(text='list', command = list_entry)
list_button.grid(row=row+1,column=2)

win.mainloop()
