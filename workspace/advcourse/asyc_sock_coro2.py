'''
Created on 02 May 2017

@author: mark
'''
import socket
import select
import logging as log
log.basicConfig(level=log.DEBUG)

def From(fn):
    pass 

def connect_coro(url):
    sock = socket.socket()
    fno = sock.fileno()
    log.debug(fno)
    sock.connect((url,80))
    sock.setblocking(0)
    log.debug('connect')
    while True:
        yield
        log.debug(select.select([fno], [fno], [fno]))
        if fno in select.select([fno], [fno], [fno])[1]:
            sock.send('GET / HTTP/1.0\n\n\n')
            break
    while True:
        yield
        log.debug(select.select([fno], [fno], [fno]))
        if fno in select.select([fno], [fno], [fno])[0]:
            print sock.recv(2000)
            break
    sock.close()

coro1 = connect_coro('ledge.co.za')
coro2 = connect_coro('google.com')

while True:
    next(coro1)
    next(coro2)