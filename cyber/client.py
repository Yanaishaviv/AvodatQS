import socket
import RSA
import constants


def send_str_data(server, data):
    message = str.encode(data)
    server.send(message)

def recieve_data(server_socket):
    while True:
        message = server_socket.recv(1024)
        if message != b'':
            return message.decode()



if __name__ == '__main__':

    my_socket = socket.socket()
    my_socket.connect((constants.SERVER_IP, constants.SENDER_PORT))

    # start_connection = "asking for public key"
    # bytes1 = str.encode(start_connection)

    # my_socket.send(bytes1)

    public_key_0 = int.from_bytes(my_socket.recv(1024), 'big')
    public_key_1 = int.from_bytes(my_socket.recv(1024), 'big')
    public_key = (public_key_0, public_key_1)
    encr_mes = RSA.encrypt(public_key, input("enter message: "))
    sec_socket = socket.socket()
    sec_socket.connect((constants.SERVER_IP, constants.RECIEVER_PORT))
    sec_socket.send(str.encode(encr_mes.__str__()))
    # print(my_socket.recv(2123))
    print("sent success")
    print(my_socket.recv(1024))

    mess = str.encode('stop')
    sec_socket.send(mess)
