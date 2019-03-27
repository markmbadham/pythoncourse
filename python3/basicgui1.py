#!/usr/bin/env python
import Tkinter as tk
win = tk.Tk()
sides = ['bottom','left','right','top']
rows=1
cols=0
buttons = {}
for button_text  in ('Push','Press','Self destruct','top'): 
    cols +=1
    if cols%3==0:
        cols=1
        rows+=1
    button = tk.Button(text=button_text + "(%d,%d)" % (cols,rows))
    button.grid(row=rows, column=cols)
    buttons[button_text] = button

buttons['Self destruct']['command'] = quit
win.mainloop() 
