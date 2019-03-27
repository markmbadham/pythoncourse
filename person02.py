from person01 import Person,test_person

class EmailUser(object):
    def send_mail(self):
        pass

class Employee(Person, EmailUser):
    persons = 0
    
    def  __init__(self, name='', age=0, job=''):
        Person.__init__(self, name, age)
        self.job = job
        Employee.persons += 1
        self.empid = Employee.persons

    def work(self):
        return "id do the work of a %s" % self.job

if __name__ == '__main__':
    emp = Employee('Fred',30, 'plummer')
    print(test_person(emp))
    print(emp.job)
    print(emp.work())
    print(emp.empid)
    emp.send_mail()
