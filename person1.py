class Person(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        return 'hello my name is %s' % self.name

    def walk(self):
        if self.age < 1 : return "crawl"
        elif self.age < 75: return "walk"
        else : return "hobble"

    def get_name(self):
        return self.firstname + ' ' + self.surname

    def set_name(self, name):
        try:
            self.firstname, self.surname = name.split(' ')
        except ValueError:
            self.firstname = name
            self.surname = ""

    name = property(get_name, set_name)

def test_person(name, age):
   person = Person(name=name,age=age)
   print(person.talk()) 
   print(person.walk()) 
   return person

test_person('fred',10)
test_person('sally',0.7)
harry = test_person('harry casual',80)
print(harry.name,harry.firstname,harry.surname)
