import tkinter as tk
import server_send

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        


    def create_widgets(self):
        self.msg = tk.StringVar()
        self.msg.set("type here")
        self.create_msg_list()
        self.create_input(self.msg)
        self.add_quit_button()


    def create_input(self, str_var):
        self.inp = tk.Entry(self, textvariable = str_var)
        self.inp.pack()
        self.add_send_button()

    def add_send_button(self):
        self.send_button = tk.Button(self)
        self.send_button["text"] = "send message"
        self.send_button["command"] = self.get_input
        self.send_button.pack(side="top")


    def create_msg_list(self):
        self.msg_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.msg_frame)
        self.msg_list = tk.Listbox(self.msg_frame, height = 15, width = 50, yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.msg_list.pack(side = tk.LEFT, fill = tk.BOTH)
        self.msg_list.pack()
        self.msg_frame.pack()


    def add_quit_button(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


    def get_input(self):
        #event.widget["activeforeground"] = "red"
        data = self.inp.get()
        print(data)
        self.msg_list.insert(tk.END, data)
        self.msg.set("")




root = tk.Tk()
app = Application(master=root)
app.master.title("Yanai's chat")
# app.master.minsize(1000,400)
app.mainloop()
