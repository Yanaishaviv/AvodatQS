import socket

my_socket = socket.socket()
my_socket.connect(("localhost", 35491))

HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
bytes1 = str.encode(HTTPMessage)

my_socket.sendall(bytes1)
my_socket.close()