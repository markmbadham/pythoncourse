#!/usr/bin/env python

config = open('config.text')
for line in  config:
    if line.startswith('host'):
          print line[line.index('=')+1:]

config.seek(0)
for line in  config:
    if line.startswith('host'):
          print line.split('=')[1]

config.seek(0)
for line in  config:
    (key,val)= line.split('=')
    if key.strip() == "host":
        print val.strip()

import re
config.seek(0)
for line in  config:
    (key,val)= re.split('\s*=\s*',line)
    if key == "host":
        print val

config.seek(0)
for line in  config:
    match=re.search('host\s*=\s*(.*)',line)
    if match:
        print match.group(1) 

config.seek(0)
match = re.search('host\s*=\s*(.*)', config.read())
if match:
    print match.group(1)

#creating dict
conf = {}

config.seek(0)
for line in  config:
    match=re.search('\s*(.*)\s*=\s*(.*)',line)
    if match:
        conf[match.group(1)] = match.group(2)

print conf


