'''
Created on 12 Jun 2014

@author: mark
'''
import socket
from threading import Thread

class EchoServer(Thread):
    running = True
    lsock = socket.socket()
    
    def __init__(self,sock=None):
        Thread.__init__(self)
        if sock : self.sock = sock
        
    def setup(self):
        try:
            EchoServer.lsock.bind(('127.0.0.1',10002))
            EchoServer.lsock.listen(5)
            while EchoServer.running:
                (bsock,add) = EchoServer.lsock.accept()
                new_server = EchoServer(bsock)
                new_server.start()
        finally:
            EchoServer.lsock.close()
           
    def run(self):
        try:
            self.sock.send("Welcome\r\n")
            line=''
            while not line.startswith("quit"):
                line = self.sock.recv(4096)
                print line
                self.sock.send(line)
        finally:
            self.sock.close()
                
if __name__ == "__main__":
    EchoServer().setup()