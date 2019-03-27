'''
Created on 8 May 2018

@author: mark
'''

print(a,
      b)

def greeter(name, surname=''):
    return "hello world %s %s" % (name, surname)

print greeter('fred')    #function call 
print greeter('a', 'b')    # second function call
print greeter('c')

def interest(principle, rate, nper):
    if type(rate) == int:
        rate = rate/100.0
    return principle * (1 + rate)**nper

print interest(1000, 12, 36)

def graph(lst, LABELS=None):
    out = []
    for i,e in enumerate(lst):
        if LABELS:
            label = LABELS[i]
        else: label = e
        out.append(label.ljust(10) + ('*' * e))
    return '\n'.join(out)
        
#graph([3,2,5,1,9])

def random_test():
    import random
    results = [0]*10
    for i in range(500):
      rnd =  random.randint(0,9)
      results[rnd] += 1
    return results

#results = random_test()
#graph(results)
#print results
        