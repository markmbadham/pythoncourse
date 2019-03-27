#! /opt/anaconda/bin/python

class Relhum(object):
    def __init__(self,tmp="",rh=""):
        self.rh=rh      
        self.tmp=tmp
    
    def dew(self):
        self.tmpc=self.tmp-273.15
        self.dpt=self.tmpc-(14.55+0.114*self.tmpc)*(1-0.01*self.rh)+((2.5+0.007*self.tmpc)*(1-0.01*self.rh))**3+(15.9+0.117*self.tmpc)*(1-0.01*self.rh)**14
        return "Dewpoint is "+str(self.dpt)

if __name__=="__main__":
        r1=Relhum(289.15,99)
        print r1.dew()
