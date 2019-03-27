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

def tree1(rows=5)
    return '\n'.join(map(lambda n: (n*'* ').center(2*rows), 
            range(1,rows+1)))

def sum(*args):
    out = 0
    for arg in args:
        out += arg
    return out

if __name__ == '__main__':
    print sum(1,2,3,4)
