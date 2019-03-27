class Person(object):
   def __init__(self,name='',age=0):
      self.name =  name
      self.age = age
   
   def get_name(self):
      return  self.fname + ' ' +self.sname
   
   def set_name(self,name):
      if ' ' in name:
          self.fname, self.sname = name.split(' ')
      else: 
          self.fname, self.sname = (name,'')

   name = property(get_name, set_name)

   def talk(self):
      return 'hello my name is %s' % self.__dict__.get('name')
    
   def walk(self):
      if self.age < 1 : return '4 legs'
      elif self.age < 75 : return '2 legs'
      else : return '3 legs'
   '''   
   def __setattr__(self, name,val):
       self.__dict__[name] = val

   def __getattribute__(self, name):
       if name == 'name':
           return self.__dict__['fname'] + ' ' + self.__dict__['sname']
       else:
           return object.__getattribute__(self,name) 
   '''
class EmailUser(object):
    def email(self, to_address, date):
        return '''FROM:<%s>
                  TO:<%s>
                  DATE:<%s>
                  Message''' % (self.__dict.get('address'), to_address, date)

class Employee(Person):
    employees = 0
    def __init__(self,name='', age=0, job=''):
        self.job = job
        Person.__init__(self,name,age)
        Employee.employees +=1
        employee_no = Employee.employees

    def work(self):
        return "i am %sing " % self.job

    
if __name__ == '__main__':
    fred = Person(name="Fred Basset", age=10)
    bob = Employee(name="bob Basset", age=20, job ="janitor")
    sally = Person(name="Sally Derkins", age=0.5)
    print(fred.talk())
    print(fred.walk())
    print(sally.talk())
    print(sally.walk())
    print(bob.talk())
    print(bob.walk())
    print(bob.work())
