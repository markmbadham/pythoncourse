class Foo(object):
    _private = 'test'
    a = 10
    b = 20
    def __init__(self):
        self.x = 10

    def show_x(self):
        print(self.x)

    def alter(self):
       Foo.a += 10

if __name__ == '__main__':
    foo = Foo()
    foo2 = Foo()
    foo2.x += 1
    foo.show_x()
    foo2.show_x()
