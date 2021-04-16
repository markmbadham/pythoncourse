import logging as log
FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
log.basicConfig(format=FORMAT, filename='test.log', level=log.DEBUG)
log.debug('start')
try:
   1/0
except ZeroDivisionError:
    log.exception('Cannot divide by zero')
try:
    a
except NameError:
    log.exception('name not known')
try:
   number = int(input('Enter a number: '))
except ValueError as e:
    log.error('that was not a number %s' % e)

print('Carrying on')