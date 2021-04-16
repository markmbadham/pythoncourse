from socket import socket

server_socket = socket()
try:
    server_socket.bind(('0.0.0.0', 10003))
    server_socket.listen(5)
    sock, address = server_socket.accept()
    sock.send(b'Welcome to the dark web\n')
    while True:
        line = sock.recv(8194)
        print(line)
        sock.send(line.upper())
        if line.strip() == b'quit':
            break
    sock.close()
finally:    
    server_socket.close()