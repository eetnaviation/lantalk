import socket
import threading
import tkinter
from tkinter import simpledialog

msg = tkinter.Tk()
#ipmsg = simpledialog.askstring("IP", "Enter server IP: ", parent=msg)
#portmsg = simpledialog.askstring("Port", "Enter server port: ", parent=msg)
user = simpledialog.askstring("Username", "Enter name: ", parent=msg)
SERVER_HOST = '192.168.1.252'
SERVER_PORT = 5002
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))


Tk = tkinter.Tk
root = Tk()
window = Tk()
window.title("Lan Talk")
window.configure(width=500, height=300)
window.configure(bg='lightgray')
l = Label(root, text = "allllllllllllllllllllllllllllllllll")
l.config(font =("Courier", 14))
window.mainloop()

