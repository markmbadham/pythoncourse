#! /usr/bin/env python
def square(x):
    '''
    >>> square(4)
    64
    >>> square(2)
    4
    '''
    return x**2

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
       _test()

