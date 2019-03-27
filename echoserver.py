import socket
import logging as log
import traceback as tb
from threading import Thread

FORMAT = '%(asctime)s:%(levelname)s:%(thread)d:%(message)s'
log.basicConfig(format=FORMAT, filename='server.log', level=log.DEBUG)

class EchoServer(Thread):

    ssock = socket.socket()
    running = True

    def __init__(self, sock=None):
        Thread.__init__(self)
        if sock:
            self.sock = sock
            self.start()
        else:
            log.info('starting')
            self.setup()

    def setup(self):
        try:
            ssock = EchoServer.ssock
            ssock.bind(('127.0.0.1',10001))
            log.debug('bound to port')
            ssock.listen(5)
            while (EchoServer.running):
                (sock,address)=ssock.accept()
                #log.debug('connection accepted from %s' % address)
                log.debug(address)
                new_server = EchoServer(sock)
        except:
            log.error(tb.format_exc())
        finally:
            ssock.close()
    
    def run(self):    
        self.sock.send('Welcome\n')
        while(True):
            line = self.sock.recv(8192)
            log.debug('recvd: %s' % line)
            self.sock.send(line)
            if line.strip() == 'quit': break
        self.sock.close()
        log.debug('connection closed')

if __name__ == '__main__':
    EchoServer()
