'''
Created on 16 Aug 2017

@author: mark
'''
class Person(object):
    
    def __init__(self):
        self.name = ''
        self.age = 0
        
    def talk(self):
        return 'hello my name is {}'.format(self.name)
    
    def walk(self):
        age = self.age
        if age < 1:
            return "crawl"
        elif age <75:
            return "walk"
        else:
            return "hobble"

if __name__ == '__main__':
    fred = Person()
    fred.name = 'Fred'
    fred.age = 10
    print(fred.talk(), fred.walk())
