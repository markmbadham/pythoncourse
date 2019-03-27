'''
  General functions module

'''
def greeter(name, surname=''):
    '''
    function greeter retunrs a greeting
    >>> greeter('fred')
    'hello fred'
    >>> greeter('bob', 'cratchet')
    'hello bob cratchet'
    '''
    return "hello %s %s" % (name, surname)

def test_args(x, *args, **kwargs):
    print(args, kwargs)

def ave(*args):
    '''
    function ave returns the average of args
    >>> ave(1,2,3,4,5)
    3.0
    '''
    return sum(args) / len(args)
    
def make_double(fn):
    def inner(*args, **kwargs):
        return 2 * fn(*args, **kwargs)
    return inner

def square(x):
    '''
    >>> [square(x) for x in range(10)]
    [0, 1, 4, 9, 17, 25, 36, 49, 64, 81]
    '''
    return x**2

def updown(n):
    for i in range(n): 
        yield i
    for i in range(n, 0, -1):
        yield i

def itersdin(quit):
    while True:
       line = input()
       yield line
       if line == quit:
           break

def get_int(message):
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("Not an int")
        else:
            return value

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()