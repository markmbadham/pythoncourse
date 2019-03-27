import tkinter as tk
from gui02 import Form
class Form2(Form):
    def setup(self):
       for title in ['username','password']:
           self.add_row(title)
           self.button = tk.Button(text='print', command=self.button_action)
           self.button.grid(column=2, row=self.rows+1)
if __name__ == "__main__":
    Form2()
