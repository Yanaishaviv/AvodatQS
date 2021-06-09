import constants
import RSA
import AES
import server
import threading
import functions
import server

class server_obj(threading.Thread):
    def __init__(self, thread_id, name, port, private_key = None, sender = False):
        threading.Thread.__init__(self)
        self.thread_id = thread_id 
        self.name = name
        self.ip = functions.get_ip()
        self.port = port
        self.server_socket = server.build_socket(my_ip = self.ip, my_port = self.port)
        self.sender = sender
        if not sender:
            self.private_key = private_key

    def run(self):
        if not self.sender:
            print("starting reader", self.name)
            (client_connection, client_address) = server.accept_client(self.server_socket)
            self.cli_con = client_connection
            self.cli_adr = client_address
            encrypted_key = server.recieve_data(self.cli_con)
            self.key = server.get_from_rsa(self.private_key, encrypted_key)
        else:  
            print("starting sender", self.name)
            (client_connection, client_address) = server.accept_client(self.server_socket)
            self.cli_con = client_connection
            self.cli_adr = client_address
            public, private = server.use_rsa()
            self.public_key = public_key
            self.private_key = private_key
            server.send_int_data(client_connection, public[0])
            server.send_int_data(client_connection, public[1])
        
    def send_message(self, data):
        encrypted_msg = AES.encrypt(self.key, data)
        server.send_str_data(self.cli_con, encrypted_msg)

    def recieve_data(self):
        encrypted_msg = server.recieve_data(self.cli_con)
        msg = AES.decrypt(self.key, encrypted_msg)
        return msg


