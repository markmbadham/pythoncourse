def square(x):
    return x*x

def fact(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out

def factr(n):
    return 1 if n <= 1 else n * factr(n-1)

def get_message(message, truncate_after=4):
    return message[:truncate_after]

def tree(n):
    print('* '*n)

tree(5)