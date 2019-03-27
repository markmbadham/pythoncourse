'''
Created on 17 May 2018

@author: mark
'''
from socket import socket
from threading import Thread

class Server(Thread): 
    RUNNING = True
    def __init__(self):
        server_socket = socket()
        try:
            server_socket.bind(('localhost',10002))
            server_socket.listen(6)
            while Server.RUNNING:
                Worker(server_socket.accept()).start()
        except Exception as e:
            print(e)
        
        finally:
            server_socket.close()

class Worker(Thread):
    def __init__(self, sockaddress):
        #super(Worker, self).__init__()       
        Thread.__init__(self)
        self.sock = sockaddress[0]
         
    def run(self):
        sock = self.sock
        try:
            while True:
                line = sock.recv(4096)
                if 'quit' in line:
                    break
                elif 'shutdown' in line:
                    Server.RUNNING = False
                    break
                sock.send(line + '\n')
        except Exception as e:
            print(e)
        finally:
            sock.close()
                    
if __name__ == '__main__':
    Server()
