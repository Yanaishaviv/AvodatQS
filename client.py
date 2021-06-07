import socket
import RSA

my_socket = socket.socket()
my_socket.connect(("10.0.0.4", 35491))

start_connection = "asking for public key"
bytes1 = str.encode(start_connection)

my_socket.send(bytes1)

public_key_0 = int.from_bytes(my_socket.recv(1024), 'big')
public_key_1 = int.from_bytes(my_socket.recv(1024), 'big')
public_key = (public_key_0, public_key_1)
encr_mes = RSA.encrypt214(public_key, input("enter message: "))
my_socket.send(str.encode(encr_mes.__str__()))
# print(my_socket.recv(2123))
print("sent success")

mess = str.encode('stop')
my_socket.send(mess)
