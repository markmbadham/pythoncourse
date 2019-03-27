#!/usr/bin/env python
'''
Gets the username part of an email
'''

email = raw_input('enter your email: ')
print email[:email.index('@')]


