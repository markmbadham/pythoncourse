def square(x, y=2):
    return x**y

def tree(n):
    out = []
    for i in range(1,n+1):
        out.append(('* '*i).center(n*2))
    return '\n'.join(out)

def sum(arr):
    out = 0
    for i in arr: out += i
    return out

def fact(n):
    out = 1
    #for i in range(n,0,-1): out*=i
    for i in range(1,n+1): out*=i
    return out

def factr(n):
    if n>1: return n*factr(n-1)
    else: return 1

def factr2(n):
    return n*factr(n-1) if n>1 else 1

def make_double(fn):
    def inner(*args,**kwargs):
        return fn(*args,**kwargs)*2
    return inner



