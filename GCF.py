def is_factor(n, f):
    return n % f == 0

def gcf(args):
    args.sort()
    possible_factors = range(2,min(args) + 1)
    for arg in args:
        print(possible_factors)
        factors = set()
        for i in possible_factors:
            print('arg',arg,'i',i)
            if is_factor(arg, i):
                factors.add(i)
        possible_factors = factors.copy()
    return factors
    
print(gcf([100,30,10]))
        