import socket
import traceback as tb
from threading import Thread
import logging as log
FORMAT = '%(asctime)s:%(levelname)7s:%(threadName)7s:%(message)s'
log.basicConfig(format=FORMAT, filename='server.log', level=log.DEBUG)

class Server(Thread):
    RUNNING = True
     
    def __init__(self,sock = None):
        Thread.__init__(self)
        if sock:
            log.debug('Starting instance')
            self.sock = sock
        else:
            log.debug('Starting main server')
            self.listen()
            
    def listen(self):
        try:
            lsock = socket.socket()
            lsock.bind(('0.0.0.0',10004))
            log.debug('bound to port')
            lsock.listen(5)
            while Server.RUNNING:
                (sock,addr) = lsock.accept()
                log.debug('accepted socket on %s:%s' % addr)
                new_server = Server(sock)
                new_server.start()
        except socket.error:
            log.error('Socket Error on listening Socket')
            log.error(tb.format_exc())
        except:
            log.error(tb.format_exc())
            for error in tb.format_stack():    
                log.error('line %d: %s' % error[1,3])
        finally:
            log.debug('Closing up shop')
            lsock.close()
            Server.RUNNING = False

    def run(self):   
        try:
            self.sock.send(b"Welcome to Echo Server 0.1")
            while Server.RUNNING:
                line = self.sock.recv(8092)
                self.sock.send(line)
                log.debug(line)
                if line.startswith(b"quit"):
                    break

        except socket.error:
            log.error('Socket Error on socket')
        except:
            log.error(tb.format_exc())
        finally:
            self.sock.close()

if __name__ == '__main__':
    Server()


