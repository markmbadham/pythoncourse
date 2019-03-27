import tkinter as tk
from Form_Class import Form
class Form2(Form):
    def button_action2(self):
        import sys
        sys.exit(0) 

    def setup(self):
        self.setup_rows('Product','Description','tests','locale')
        button = tk.Button(text='Save', command=self.button_action2)
        button.grid(row=self.rows+1,column=0)
        self.mainloop()

if __name__ == '__main__':
    win = Form2()

