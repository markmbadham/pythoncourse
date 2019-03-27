def greeter(name, surname=''):
    greeting = 'hello %s %s' % (name, surname)
    return greeting

print greeter(surname='Basset',name='fred')
print greeter(name='sally', surname='Derkins')


