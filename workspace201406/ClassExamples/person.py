'''
Created on 11 Jun 2014

@author: mark
'''
class Person(object):
    '''
    classdocs
    '''

    def __init__(self,name='',age=0):
        '''
        Constructor
        '''
        self.name = name
        self.age = age
    
    def talk(self):
        return "hello my name is %s" % self.name
    
    def walk(self):
        if self.age <=1 : return "crawling..."
        elif self.age >75: return "hobbling..."
        else : return "walking..."

class Employee(Person):
    '''
    classdocs
    '''
    last_employee_no = 0
    
    #def __init__(self,*args,**kwargs):
    def __init__(self,name,age,jobtitle):
        '''
        Constructor
        '''
        #self.jobtitle = kwargs.pop('jobtitle') if 'jobtitle' in kwargs else  ''
        self.jobtitle = jobtitle
        Employee.last_employee_no +=1
        self.employee_no = Employee.last_employee_no
        #Person.__init__(self,*args,**kwargs)
        Person.__init__(self,name,age)
        email_address = self.name+"@acme.com"
        EmailUser.__init__(self,email_address)
    
    def work(self):
        return "I am %sing" % self.jobtitle

if __name__ == '__main__':    
    isaac = Employee(jobtitle='researcher',name="Isaac")
    fred = Person(name="fred")
    print fred.talk(), fred.walk()
    sally = Person('Sally',5)
    print sally.talk()
    print sally.walk()
    print sally.__str__()
