#!/usr/bin/env python3

filename = 'config.text'

fileo = open(filename)

#Method 1
for line in fileo:
    if line.strip().startswith('port'):
        print(line.split('=')[1])
        # or
        #print line[:line.index('=')+1]

fileo.seek(0)
#Method 2
content = fileo.readlines()
line = list(filter(lambda x: x.startswith('port'),content))[0]
print(line.split('=')[1])

fileo.seek(0)
import re
#Method 3
for line in fileo:
    match =  re.search(r'^\s*port\s*=\s*(\d+)\s*$',line)
    if match:
        print(match.group(1))

fileo.seek(0)
#Method 4
content = fileo.read()
match =  re.search(r'^\s*port\s*=\s*(\d+)\s*$',content,re.M)
if match:
    print(match.group(1))


fileo.seek(0)
# create a dict
config = {}
for line in fileo:
    match =  re.search(r'^\s*(\S+)\s*=\s*(\S+)\s*$',line)
    if match:
        config[match.group(1)] = match.group(2)

print(config)








