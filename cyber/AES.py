import hashlib as hash
from Crypto import Random
from Crypto.Cipher import AES as AES1
from base64 import b64encode, b64decode
import threading

class AES():
    def __init__(self, key):
        self.block_size = AES1.block_size
        self.key = hash.sha256(key.encode()).digest()
        print("AES line 10", threading.current_thread(), self.key)

    def __pad(self, data):
        bytes_to_pad = self.block_size - len(data) % self.block_size
        pad = bytes_to_pad * chr(bytes_to_pad)
        padded_data = data + pad
        return padded_data

    @staticmethod
    def __unpad(text):
        bytes_to_unpad = ord(text[-1])
        if (bytes_to_unpad != 1 and bytes_to_unpad != ord(text[-2])):
            return text
        return text[:-bytes_to_unpad]

    def encrypt(self, text):
        text = self.__pad(text)
        iv = Random.new().read(self.block_size)
        aes_encrypter = AES1.new(self.key, AES1.MODE_CBC, iv)
        msg_to_send = aes_encrypter.encrypt(text.encode())
        return b64encode(iv + msg_to_send).decode("utf-8")

    def decrypt(self, text):
        encrypted_data = b64decode(text)
        iv = encrypted_data[:self.block_size]
        aes_decrypter = AES1.new(self.key, AES1.MODE_CBC, iv)
        readable_data = aes_decrypter.decrypt(encrypted_data[self.block_size:]).decode("utf-8")
        return self.__unpad(readable_data)


# aes = AES2("e")
# data = aes.encrypt("hello, friend")
# print(data)
# print(aes.decrypt(data))
