import tkinter as tk
import sys
def button_action():
    print('button pressed')

win = tk.Tk()
rows, cols = 1,0
for title in ['top','bottom','left', 'right']:
    cols +=1
    if cols == 3:
        cols=1
        rows+=1
    button = tk.Button(text=title, command = button_action)
    button.grid(row=rows, column=cols) 
button['command'] = lambda :sys.exit(0)

for title in ['name','surname','age']:
    rows +=1
    label = tk.Label(text=title)
    label.grid(column=1, row=rows)
    entry = tk.Entry()
    entry.grid(column=2, row=rows)

text = tk.Text()
text.grid(row=rows+1, column=1, columnspan=2)
win.mainloop()
