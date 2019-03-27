#! /usr/bin/env python
def square(x):
    '''
    >>> square(4)
    16
    >>> [square(x) for x in range(10)]
    [0, 2, 4, 9, 16, 25, 36, 49, 64, 81]
    '''
    return x**2

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
       _test()

