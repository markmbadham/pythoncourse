'''
Created on 17 Aug 2017

@author: mark
'''
import logging as log
FORMAT = '%(asctime)s:%(levelname)s:%(thread)d:%(message)s'
log.basicConfig(format=FORMAT, filename='test.log', level=log.DEBUG)

log.debug('Starting')
try:
    #int('a')
    a[1]
    1/0
    print('This will not run')
except ZeroDivisionError as e:
    log.error('cannot divide by zero',e)
except NameError:
    log.exception('err')
except Exception as e:
    print('Unknown exception',e)
else:
    print('no exception')
finally:
    print('This happens no matter what')
