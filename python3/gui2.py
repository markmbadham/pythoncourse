#!/home/mark/anaconda3/bin/python
from gui1 import GUI
class GUI2(GUI):
    filename = "out.text"
    def button_fn(self):
        file = open(GUI2.filename,'w')
        for key in self.entries:
            #file.write("%s\t%s\n" % (key,self.entries[key].get()))
            file.write(key+"\t"+self.entries[key].get()+"\n")
        file.close()

if __name__ == "__main__":
    GUI2('user','pass','db','host','port')
