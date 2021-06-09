import server
import server_obj
import gui_try
import threading.Thread
import constants

if __name__ == '__main__':
    sender_server = server_obj(
        thread_id = 0, name = "sender", port = constants.SENDER_PORT, sender = True)
    sender_server.start()
    recv_server = server_obj(thread_id = 0, name = "recv", 
        port = constants.RECIEVER_PORT, private_key = sender_server.private_key, sender = false)
    sender_server.recieve_data()