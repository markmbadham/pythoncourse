import tkinter as tk

win = tk.Tk()

text = tk.Text(win)
text.pack()
press_button = tk.Button(
    win,
    text='press',
    command = lambda : text.insert(0.0,'press')
)
press_button.pack()
push = tk.Button(
    text='push',
    command = lambda : print(text.get(0.0,tk.END))
)
push.pack()

win.mainloop()