import constants
import RSA
import AES
import server
import threading
import functions
import server

class server_obj(threading.Thread):
    def __init__(self, thread_id, name, port, public_key, private_key, 
        sender = False, even = None, app_gui = None, quit_event = None):
        threading.Thread.__init__(self)
        self.thread_id = thread_id 
        self.name = name
        self.ip = functions.get_ip()
        self.port = port
        self.server_socket = server.build_socket(my_ip = self.ip, my_port = self.port)
        self.sender = sender
        self.public_key = public_key
        self.private_key = private_key
        self.event = even
        self.app = app_gui
        self.quit_event = quit_event

    def run(self):
        print("Starting thread", self.name)
        (client_connection, client_address) = server.accept_client(self.server_socket)
        self.cli_con = client_connection
        self.cli_adr = client_address
        self.prepare_encryption()
        if not self.sender:
            self.read_chat()
        # if not self.sender:
        #     # encrypted_key = server.recieve_data(self.cli_con)
        #     # self.key = server.get_from_rsa(self.private_key, encrypted_key)
        # else:  
        #     print("starting sender", self.name)
        #     #(public, private) = server.use_rsa()
        #     # self.public_key = public
        #     print("i reached here")
        #     # self.private_key = private
        #     (client_connection, client_address) = server.accept_client(self.server_socket)
        #     self.cli_con = client_connection
        #     self.cli_adr = client_address
        #     # server.send_int_data(self.cli_con, public[0])
        #     # server.send_int_data(self.cli_con, public[1])
        
    def prepare_encryption(self):
        if self.sender:
            server.send_int_data(self.cli_con, self.public_key[0])
            server.send_int_data(self.cli_con, self.public_key[1])
            print("rsa sent")
        else:
            print("reached line 53 server obj")
            encrypted_key = server.recieve_data(self.cli_con)
            self.add_aes_key(server.get_from_rsa(self.private_key, encrypted_key))
            self.event.set()


    def add_aes_key(self, key):
        self.key = key
        self.AES = AES.AES(self.key)

    def send_message(self, data):
        encrypted_msg = self.AES.encrypt(data)
        server.send_str_data(self.cli_con, encrypted_msg)

    def recieve_data(self):
        encrypted_msg = server.recieve_data(self.cli_con)
        msg = self.AES.decrypt(encrypted_msg)
        if msg == '\quit1':
            self.quit_event.set()
            return
        if msg == '\quit':
            self.quit_event.set()
            self.app.dest(False)
            return
        self.app.insert_message(msg)
        return msg

    def read_chat(self):
        while not self.quit_event.is_set():
            self.recieve_data()
