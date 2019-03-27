class Person(object):
    def __init__(self, name='',age=0):
        self.name = name
        self.age = age
    
    def talk(self):
        return "hello my name is %s" % self.name

    def walk(self):
        if self.age < 1 : return 'crawl'
        elif self.age > 75 : return 'hobble'
        else: return 'walk'

def show_person(*persons):
    for person in persons:
        print(person.name, person.talk(), person.walk())

fred = Person('Fred',20)
harry = Person('Harry',80)
show_person(fred,harry)
