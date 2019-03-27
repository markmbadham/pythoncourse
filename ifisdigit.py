number1 = raw_input('Enter a number')
if number1.isdigit():
    number1 = int(number1)
    print number1 * 10
else: 
    print "not a number"
    print "next time enter digits"

raw_input('Press any key to exit')
