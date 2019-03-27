try:
    #print(1/0)
    #a = []
    #a[0]
    b
    'no error here'
except ZeroDivisionError:
    print('cant devide by 0')
except ArithmeticError:
    print('some maths problem')
except IndexError:
    print('index problem')
except NameError:
    print('no such name')
else:
    print('there was no error')
finally:
    print('we always do this')
print('END')
