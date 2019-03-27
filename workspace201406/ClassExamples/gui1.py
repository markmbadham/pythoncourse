'''
Created on 18 Jul 2014

@author: mark
'''
import Tkinter as tk
win = tk.Tk()
row=1
col=1
buttons = {}
for label in ['left', 'right', 'top','bottom']:
    buttons[label] = tk.Button(text=label)
    buttons[label].grid(row=row, column=col)
    col +=1
    if col ==3:
        row +=1
        col =1

buttons['top']["command"] = lambda : quit()     
win.mainloop()

#tk.Entry() tk.Label(text="")