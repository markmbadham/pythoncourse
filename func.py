def fact(x):
   result = 1
   for n in range(1,x+1):
       result *= n
   return result 

def factr(x):
   return 1 if x<=1 else x * factr(x-1)
