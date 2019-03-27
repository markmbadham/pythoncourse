# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:24:47 2017

@author: mark
"""
import logging as log
FORMAT = '%(asctime)s:%(levelname)10s:%(message)s'
log.basicConfig(format=FORMAT, filename='test.log', level=log.DEBUG)

a = []
log.debug('starting')
try:
    #a[1]
    #print(z)
    1/0
    1/1
except ZeroDivisionError as e:
    log.exception('Cannot div by zero')
except NameError as e:
    log.exception('bad name')
except Exception as e:
    print(e)
else:
    print('no exception')
finally:
    print('happens no matter what')

print('still going')