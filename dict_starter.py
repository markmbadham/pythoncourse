import sys

if len(sys.argv) > 1:
    process = sys.argv[1]
else:
    process = input('What do you want to do? (start or stop or restart) ')
if process == 'quit':
    quit()
    sys.exit(0)
result = {
    'start'  : 'starting',
    'stop'   : 'stopping',
    'restart': 'stopping\nstarting'
}
print(result.get(process.lower(),
     'usage: start|stop|restart'))