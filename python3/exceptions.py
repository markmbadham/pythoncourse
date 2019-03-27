#! /usr/bin/env python
import traceback as tb
try :
    l = []
    l[0]
    print(a)
    1/0

except ZeroDivisionError:
    print("can't devide by zero")
except NameError:
    print("name not defined")
except:
    print('an error')
    print ("err:",tb.format_exc())
    #tb.print_exc()
else:
    print('no exception occurred')
finally:
    print('we do this no matter what')

print('here the program continues')
