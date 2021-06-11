import client
import client_obj
import gui
from threading import Thread, Event
import constants
import tkinter as tk


if __name__ == '__main__':
        root = tk.Tk()
        keys = {"public" : "", 
                "aes_key": ""}
        established_connection = Event()
        stopped_connection = Event()
        established_connection.clear()
        recv_client = client_obj.client_obj(thread_id=0, name="recv_client",
                                                port = constants.SENDER_PORT, keys_dict = keys,
                                                event = established_connection,
                                                recv = True, quit_event = stopped_connection)

        recv_client.start()
        established_connection.wait()
        sender_client = client_obj.client_obj(thread_id = 0, name = "sender_client",
                                                port = constants.RECIEVER_PORT, keys_dict = keys, 
                                                recv = False)
        sender_client.start()

        app = gui.Application(master = root, sender = sender_client)

        recv_client.add_app(app)
        established_connection.wait()
        sender_client.add_aes_key()
        app.master.title("Yooda's chat")
        app.mainloop()
        stopped_connection.set()
        recv_client.socket.close()
        sender_client.socket.close()


