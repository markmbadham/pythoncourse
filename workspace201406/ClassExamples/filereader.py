'''
Created on 12 Jun 2014

@author: mark
'''
from Tkinter import * 
class FileReader(Tk):
    '''
    classdocs
    '''
    filename = '/home/mark/Documents/course/python/config.text'

    def __init__(self):
        '''
        Constructor
        '''
        Tk.__init__(self)
        self.filename_entry= Entry()
        self.filename_entry.grid(row=1,column=1)
        self.open_button = Button(text="open", command = self.open)
        self.open_button.grid(row=1,column=2)
        self.save_button = Button(text="save", command = self.save)
        self.save_button.grid(row=1,column=3)
        self.text = Text()
        self.text.grid(row=2,column=1,columnspan=3)
        self.filename_entry.insert(END, FileReader.filename)
        self.mainloop()
    def open(self):
        filename = self.filename_entry.get()
        self.text.insert(END,open(filename).read())
    
    def save(self):
        filename = self.filename_entry.get()
        save_file = open(filename,'w')
        save_file.write(self.text.get(0.0,END))
        save_file.close()

FileReader()