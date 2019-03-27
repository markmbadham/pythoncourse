import tkinter as tk
win = tk.Tk()
rows = 0
cols = 0
labels = ['Name','Surname','Age']
entries = {}
for title in labels:
    label = tk.Label(text=title)
    label.grid(row=rows, column=0)
    entry = tk.Entry()
    entry.grid(row=rows, column=1)
    entries[title] = entry
    rows+=1
def button_action():
    for key in entries:
        print(key, entries[key].get())

button = tk.Button(text='Print', command=button_action)
button.grid(row=rows+1,column=0)
win.mainloop()
