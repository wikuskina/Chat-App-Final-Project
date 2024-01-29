# Learn To Debate chat tool - LDCT - Get your host
# VS MSc IT Birkbeck 2023
# -------------------------------
# Simple program intended to be run on the computer and return host / IP address.
# User will be able to enter this IP address in the client program and connect to the server on local network.


from tkinter import *
import tkinter as tk
from tkinter import ttk
import socket

window = tk.Tk()

window.title("Get your host")
window.geometry("250x100")
window.configure(background="white")
window.resizable(False, False) 

Hostname = socket.gethostname()
# .gethostbyname returns IP address of a hostname
HOST = socket.gethostbyname(socket.gethostname())

info_label = tk.Label(window, text="Your host number:",
        font=("Arial bold", 10),
        bg="White")
info_label.pack()


host_label = tk.Label(window, state=tk.DISABLED, text=HOST,
        font=("Arial bold", 12),
        bg="White")
host_label.pack()

window.mainloop()
