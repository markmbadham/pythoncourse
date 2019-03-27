def make_double(fn):
    def inner(*args,**kwargs):
        return fn(*args,**kwargs)*2
    return inner

@make_double
def square(x,y=2):
    return x**y
#square = make_double(square)

def argify(fn):
    def inner(*args):
        return fn(args)
    return inner

@argify
def avg(args):
    return sum(args)/len(args)

def tree(n):
    out = ''
    for i in range(1,n+1):
        out += (i*'* ').center(2*n) + '\n'
    return out
    
def updown(n):
    for i in range(n): yield i
    for j in range(n,1,-1): yield j


if __name__ == '__main__':
    pass
