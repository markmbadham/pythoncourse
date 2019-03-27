def get_num(numtype,message):
    while True:
        try:
            val = numtype(raw_input(message))
        except ValueError:
            print "Not an %s" % numtype
        else:
            break
    return val

def get_int(message):
    return get_num(int,message)

def get_float(message):
    return get_num(float,message)

if __name__ == '__main__':
    i = get_int('Enter an int ')
    print i*10
    f = get_float('Enter an float ')
    print f*10
