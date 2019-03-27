import sys
print(sys.argv)

if len(sys.argv) > 1:
    process = sys.argv[1]
else:
    process = input('What do you want to do? (start or stop or restart) ')

if process == 'start':
    print('starting')
elif process == 'stop':
    print('stopping')
elif process == 'restart':
    print('stopping')
    print('starting')
else:
    print('usage: start|stop|restart')