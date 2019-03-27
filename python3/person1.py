class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        return "my name is %s" % self.name

    def walk(self):
        if self.age < 1: return 'crawl'
        elif self.age > 75: return 'hobble'
        else: return 'walk'

fred = Person(name="Fred", age=0.9)
harry = Person('Harry',90)
sally = Person('Sally',20)

for p in (fred,harry,sally):
    print(p.talk(), p.walk())
