import server
import server_obj
# import gui_try
from threading import Thread, Event
import constants

if __name__ == '__main__':
    (public, private) = server.use_rsa()
    established_connection = Event()
    established_connection.clear()
    sender_server = server_obj.server_obj(thread_id = 0, name = "sender",
        port = constants.SENDER_PORT, public_key = public, private_key = private, sender = True)
    sender_server.start()
    recv_server = server_obj.server_obj(thread_id = 0, name = "recv", 
        port = constants.RECIEVER_PORT, public_key = public, private_key = private, sender = False)
    recv_server.start()
    