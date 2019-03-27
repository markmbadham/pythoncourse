import tkinter as tk

win = tk.Tk()
buttons = {}
# def action():
#     print()
# for title in ['left', 'right', 'top', 'bottom']:
#     button = tk.Button(text=title, command = action)
#     buttons[title] = button
#     button.pack(side=title)
# buttons['top']['command'] = quit
entries = {}
for row, title in enumerate('name surname age'.split()):
    label = tk.Label(text=title)
    label.grid(row=row, column=1)
    entry = tk.Entry()
    entry.grid(row=row, column=2)
    entries[title] = entry
def print_buttons():
    for title in entries:
        print(title, entries[title].get())
button = tk.Button(text='print', command=print_buttons)
button.grid(row=row+1, column=1, columnspan=2)
win.mainloop()
