import socket

server_socket = socket.socket()
ip = "127.0.0.1"
port = 35491
server_socket.bind((ip, port))
print("Server socket bound with with ip {} port {}".format(ip, port))
print(server_socket.__str__())
flag = True
server_socket.listen()
while flag:
    (user1_conn, user1_addr) = server_socket.accept()
    while True:
        data = user1_conn.recv(1024)
        if data != b'':
            print(data.decode())
            user1_conn.send(str.encode("hi"))
        if data == b'stop':
            flag = False
            break
server_socket.close()
print("wow, can't believe this worked")
