import socket
import RSA
import constants
import functions


def use_rsa():
    '''
    hello, is this working?
    '''
    prime_num1 = functions.find_prime(constants.BITS_FOR_RSA) 
    # rsa needs two prime numbers to calculate
    prime1 = int(prime_num1)
    prime_num2 = functions.find_prime(constants.BITS_FOR_RSA) 
    prime2 = int(prime_num2)
    # i'm using one file to hold all RSA related functions
    return RSA.generate_keypair(prime1, prime2)


def build_socket(my_ip = functions.get_ip(), my_port = constants.SENDER_PORT):
    server_socket = socket.socket()
    ip = my_ip
    port = my_port
    server_socket.bind((ip, port))
    server_socket.listen()
    return server_socket
    

def accept_client(server_socket):
    (client_connection, client_address) = server_socket.accept()
    return (client_connection, client_address)


def recieve_data(client_connection):
    while True:
        message = client_connection.recv(1024)
        if message != b'':
            return message.decode()            


def send_str_data(client_connection, data):
    message = str.encode(data)
    client_connection.send(message)


def send_int_data(client_connection, data):
    message = data.to_bytes(10, 'big')
    client_connection.send(message)

def get_from_rsa(private, encrypted_msg):
    data = functions.parse_string_data(encrypted_msg)
    return RSA.decrypt(private, data)

# server_socket = socket.socket()
# ip = "0.0.0.0"
# port = 35491
# server_socket.bind((ip, port))
# print("Server socket bound with with ip {} port {}".format(ip, port))
# print(server_socket.__str__())
# flag = True
# public, private = use_rsa()
# server_socket.listen()
# while flag:
#     (user1_conn, user1_addr) = server_socket.accept()
#     while True:
#         data = user1_conn.recv(1024)
#         if data != b'':
#             print(data.decode(), user1_addr)
#             user1_conn.send(public[0].to_bytes(10, 'big'))
#             user1_conn.send(public[1].to_bytes(10, 'big'))
#             # user1_conn.send(input().encode())
#         if data == 'stop'.encode():
#             flag = False
#             break
# server_socket.close()
# print("wow, can't believe this worked")


# if __name__ != '__main__':
#     server_socket = build_socket()
#     (client_connection, client_address) = accept_client(server_socket)
#     entry = recieve_data(client_connection)
#     print(entry)
#     public, private = use_rsa()
#     send_int_data(client_connection, public[0])
#     send_int_data(client_connection, public[1])
#     encrypted_msg = recieve_data(client_connection)
#     data = functions.parse_string_data(encrypted_msg)
#     print(encrypted_msg)
#     print(RSA.decrypt(private, data))
#     server_socket.close()
