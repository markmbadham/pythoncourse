import tkinter as tk

win = tk.Tk()
# for text in 'top bottom left right'.split():
#         button = tk.Button(text=text)
#         button.pack(side=text)
buttons = {}
text = {}
for row in (1,2):
        for col in (1,2):
            text['{}{}'.format(row,col)] = 'row={} col={}'.format(row,col)
            button = tk.Button(text=text,
                            command=lambda :print("button {} pressed".format(text['{}{}'.format(row,col)])))
            button.grid(row=row, column=col)
            buttons['{}{}'.format(row,col)] = button
def button_command():
    print('great')
buttons['22']['command'] = button_command

win.mainloop()