#!/usr/bin/env python
import Tkinter as tk

class BasicWin(tk.Tk):    

    def __init__(self):
        tk.Tk.__init__(self)
        self.text = tk.Text()
        top_frame = tk.Frame()
        top_frame.pack(side="top")
        self.open_button = tk.Button(top_frame,text="open", 
                        command=self.open_action)
        self.save_button = tk.Button(top_frame,text="save", 
                        command=self.close_action)
        self.open_button.pack(side="left")
        self.save_button.pack(side="right")
        self.text.pack(side="bottom")
        self.mainloop()

    def open_action(self):
        self.text.insert(0.0,"open")
    def close_action(self):
        print self.text.get(0.0,tk.END)

if __name__ == "__main__":
    BasicWin()
