import threading
import server
import server_obj
import gui
from threading import Thread, Event
import constants
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    (public, private) = server.use_rsa()
    established_connection = Event()
    stopped_connection = Event()
    established_connection.clear()
    sender_server = server_obj.server_obj(thread_id = 0, name = "sender",
        port = constants.SENDER_PORT, public_key = public, private_key = private, 
        sender = True)
    sender_server.start()
    app = gui.Application(master = root, sender = sender_server, event = stopped_connection)
    recv_server = server_obj.server_obj(thread_id = 0, name = "recv", 
        port = constants.RECIEVER_PORT, public_key = public, private_key = private, 
        sender = False, even = established_connection, app_gui = app, quit_event = stopped_connection)
    recv_server.start()
    established_connection.wait()
    sender_server.add_aes_key(recv_server.key)
    app.master.title("Yanai's chat")
    app.mainloop()
    stopped_connection.set()
    print(threading.enumerate())
    print(stopped_connection)
    recv_server.server_socket.close()
    sender_server.server_socket.close()

    
