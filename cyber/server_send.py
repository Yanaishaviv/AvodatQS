import constants
import RSA
import AES
import server
import threading
import functions
import server

class server_send(threading.Thread):
    def __init__(self, thread_id, name, port, private_key):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.ip = functions.get_ip()
        self.port = port
        self.server_socket = server.build_socket(my_ip = self.ip, my_port = self.port)
        self.private_key = private_key

    def run(self):
        print("starting", self.name)
        (client_connection, client_address) = server.accept_client(self.server_socket)
        self.cli_con = client_connection
        self.cli_adr = client_address
        encrypted_key = server.recieve_data(self.cli_con)
        self.key = server.get_from_rsa(self.private_key, encrypted_key)
    
    def send_message(self, data):
        encrypted_msg = AES.encrypt(self.key, data)
        server.send_str_data(self.cli_con, encrypted_msg)
        

