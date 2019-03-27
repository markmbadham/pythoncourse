'''
gui03
@VERSION 0.2
@author mark
Example Tkinter program
'''
import tkinter as tk

class FileReader(tk.Tk):
    '''
    Class that implements a file read and write
    '''
    def __init__(self):
        '''
        Constructor creates a window with:
        an enrty for the file name 
        a open button
        and a close button
        '''
        tk.Tk.__init__(self)
        self.text = tk.Text()
        self.file_entry = tk.Entry()
        self.open_button = tk.Button(text='open', command=self.open_file)
        self.close_button = tk.Button(text='close', command=self.save_file)
        tk.Label(text='File Name').grid(row=1,column=1)
        self.file_entry.grid(row=1,column=2)
        self.open_button.grid(row=1,column=3)
        self.close_button.grid(row=1,column=4)
        self.text.grid(row=2,column=1,columnspan=4)
        self.mainloop()

    def open_file(self):
        '''
        Callback methon for the open button
        uses the entry to get filename, opens the file and places content in the
        text widget
        '''
        self.text.insert(0.0,open(self.file_entry.get()).read())

    def save_file(self):
        '''
        Callback method for the save button
        uses entry for the filename and gets all the content of the tetx widget
        and writes it to the file
        '''
        open(self.file_entry.get(),'w').write(self.text.get(0.0,tk.END))

if __name__ == '__main__':
    FileReader()
