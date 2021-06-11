import constants
import client
import socket 
import threading
import random
import AES
import RSA

class client_obj(threading.Thread):
    def __init__(self, thread_id, name ,port, keys_dict, recv, event = None, quit_event = None):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.port = port
        self.recv = recv
        self.event = event
        self.quit_event = quit_event
        self.keys = keys_dict
        self.ip = constants.SERVER_IP
        self.socket = socket.socket()
    
    def run(self):
        self.socket.connect((self.ip, self.port))
        self.prepare_encryption()
        if self.recv:
            self.read_chat()
        
    def prepare_encryption(self):
        if self.recv:
            public_key_0 = int.from_bytes(self.socket.recv(1024), 'big')
            public_key_1 = int.from_bytes(self.socket.recv(1024), 'big')
            public_key = (public_key_0, public_key_1)
            self.keys['public'] = public_key
            self.keys['aes_key'] = bin(random.getrandbits(constants.BITS_FOR_RSA))
            self.AES = AES.AES(self.keys['aes_key'])
            self.event.set()

        else:
            encr_mes = RSA.encrypt(self.keys['public'], self.keys['aes_key'])
            self.socket.send(str.encode(encr_mes.__str__()))
    
    def add_aes_key(self):
        self.AES = AES.AES(self.keys['aes_key'])

    def add_app(self, app):
        self.app = app

    def recieve_data(self):
        encrypted_msg = client.recieve_data(self.socket)
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

    def send_message(self, msg):
        encrypted_msg = self.AES.encrypt(msg)
        client.send_str_data(self.socket, encrypted_msg)

    
