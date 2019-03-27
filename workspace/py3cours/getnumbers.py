'''
Created on 17 Aug 2017

@author: mark
'''
def get_num(message, numtype=int):
    while(True):
        try:
            new_num = numtype(input(message))
        except ValueError:
            print('Not an {}'.format(numtype))
        else:
            return new_num

def get_int(message):
    return get_num(message, int)
def get_float(message):
    return get_num(message, float)

if __name__ == '__main__':
    print(get_int('Enter an int: '))