#!/home/mark/anaconda3/bin/python

import tkinter as tk, sys

win = tk.Tk()
top_frame = tk.Frame(win)
top_frame.pack(side="top")
cols = 0
for title in ['b1','b2','b3','b4']:
    b = tk.Button(top_frame,text=title)
    cols +=1
    b.grid(row=1,column=cols)
text = tk.Text(win)
text.pack(side="bottom")
text.insert(tk.END,"hello")
win.mainloop()

