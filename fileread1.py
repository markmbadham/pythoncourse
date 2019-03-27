#!/usr/bin/env python3

def get_port():
    for line in open('config.text'):
        line = line.strip()
        if line.startswith('port'):
            return line.split('=')[1].strip()


def get_port2():
    configfile = open('config.text')
    for line in configfile:
        line = line.strip()
        if 'port' in line:
            return line[line.find('=')+1:]


print(get_port()) 
