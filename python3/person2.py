class Person(object):
    name = property(get_name,set_name)

    def set_name(self,name):
        self.firstname,self.surname = name.split(' ')

    def get_name(self):
        return(self.firstname + ' ' + self.surname)

    def __setattr__(self,attr,val):
        assert not attr.startswith('_'), "private var"
        self.__dict__[attr] = val

    def __init__(self,name='',age=0, firstname='',surname=''):
        self.firstname,self.surname = name.split(' ')
        self.firstname = firstname
        self.surname = surname
        self.age = age

    def talk(self):
        return "my name is %s" % self.name

    def walk(self):
        if self.age < 1: return 'crawl'
        elif self.age > 75: return 'hobble'
        else: return 'walk'

class Employee(Person):
    def __init__(self,name='',age=0,jobtitle=''):
        Person.__init__(self,name,age)
        self.jobtitle=jobtitle

    def work(self):
        return "I am %s" % self.jobtitle

if __name__ == "__main__":
    fred = Person(name="Fred", age=0.9)
    harry = Person('Harry',90)
    sally = Person('Sally',20)

    for p in (fred,harry,sally):
        print(p.talk(), p.walk())
