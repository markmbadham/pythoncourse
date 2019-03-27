'''
Created on 9 May 2018

@author: mark
'''
class Person(object):
    def __init__(self, name):
        self.name = name
        self.phone_num = ''
        self.address =  Address()
        print "init"
    def purchase_parking_pass(self):
        pass

class Address(object):
    def __init__(self):
       self.street = ''
       self.city = ''
       self.pcode = ''
       
    def validate(self):
        return True
    
    def __str__(self):
        return '\n'.join(((self.street, self.city, self.pcode)))

person1 = Person('Fred')
person1.address.street = '1 Bowling Ave'
person1.address.city = 'CPT'
person1.address.pcode = '7405'
print person1.address
person2 = Person('Jason')
print person2.name

