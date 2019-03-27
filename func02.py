def greeter(name, surname=''):
    greeting = 'hello %s %s' % (name, surname)
    return greeting

def square(x):
    return x**2

def tree(rows=5):
    out = [] 
    for n in range(1,rows+1):
        out.append((n*'* ').center(2*rows))
    return '\n'.join(out)

if __name__ == '__main__':
    print tree()
    print greeter(surname='Basset',name='fred')
    print greeter(name='sally', surname='Derkins')
    print square(3)
