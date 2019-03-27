#!/usr/bin/env python
import Tkinter as tk
from basicgui2 import BasicWin
class FileRead(BasicWin):    

    def open_action(self):
        self.text.insert(0.0,open('config.text').read())
    def close_action(self):
        open('config.text','w').write(self.text.get(0.0,tk.END))

if __name__ == "__main__":
    FileRead()
