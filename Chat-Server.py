# Learn To Debate chat tool - LDCT - SERVER SIDE
# VS MSc IT Birkbeck 2023
# -------------------------------

# Summary:
# This is a server side of the program that is run first.
# The client (local or Internet) connects to the server via specified port and host.
# Client and server send and receive messages to / from each other.
# Server side checks messages against a list of Words, from the specified file.
# This script holds a list of quotes that are shown to the user when they end chat.

# Imports
import socket
import threading
import os 
import random

# Changing working directory of Python to where the script is located, to enable file opening.
os.chdir(os.path.dirname(__file__))
# print("THIS IS DIRECTORY" + os.getcwd()) # Test

# AF_INET for IPv4 addresses, with a format of host and port number.
# SOCK_STREAM: TCP socket. 
# To enable hosts to establish a connection and exchange data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket option SO_REUSEADDR lets socket to forcibly bind to a port used by another socket.
# 1 = True
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# To connect via "0.0.0.0" - to all IPv4 addresses on the device.
# IP where server is running on author's device: local 192.168.0.22, outside ***.
HOST = "0.0.0.0"
PORT = 12345
HOST_length = len(HOST)
PORT_length = len(str(PORT))

# List of clients connected
connected_sockets = []

# Quotes prompted if user uses specific words 
promptQuotes = ["Remember, raise your words, not your voice.", "Say what you mean, but don't say it mean.",
"The goal of debate or conversation is not triumph, but advancement.",
"Better reasoning, not idea repression, is the remedy for a flawed argument.",
"Insults are the arguments of malice; arrogance is not logic.","If you cannot find a better argument - come back later."]

# Main function of the server
def main_server():
    # Binds the server
    # Client is using connect() call, server is using bind() call

    if HOST_length != 0 and PORT_length != 0:
        server.bind((HOST, PORT))
        print(f"Server binded successfully. HOST: {HOST}, PORT: {PORT}")
    else:
        print(f"No host or port provided.")

    # Listening, standard 5 "unaccepted connections" limit for the server to listen to
    server.listen(5)

    print(f'SERVER: Listening for incoming connections on HOST: {HOST} PORT: {PORT}...')

    # Client_socket = socket of the client side, addr = its address, accepted by server.
    while 1:
        client_socket, address = server.accept()

        # socket.accept() returns a tuple (conn, addr) where conn is a new socket object
        print(f"Connection from {address[0]} {address[1]} has been established.")

        # Creates a thread that runs the client_connect function along with the main function
        # Every time client_socket is connected a new tread is created and keeps running
       
        threading.Thread(target=client_connect, args=(client_socket,)).start()

# Function to receive clients
# It is started by Main function
# When username is provided (not empty), connects the client and notifies all connected clients 
# It starts a thread listen_messages_all 
def client_connect(client_socket):
    while 1:
        username = client_socket.recv(1024).decode("utf-8")
        if not username:
            break
        else:
            if username != "":
                connected_sockets.append((username, client_socket))
                notify = username + "%" + "has joined the chat."
                send_messages_all(notify)
                break
            else:
                print("Error: no username provided")


    threading.Thread(target=listen_messages_all, args=(client_socket, username,)).start()


# Function to listen for messages from client by username
def listen_messages_all(client_socket, username):
    # While loop runs and listens
    # When user clicks "End Chat" button on client side, client sends "bytes" with "&&&&"
    # Once "&&&&" is received by the server, it will be commanded to close the connection
    # Before "&&&&" is received, it is continuosly running and sending messages to connected clients
    while 1:
        try:
            message= client_socket.recv(1024).decode("utf-8")
        except:
            print ("<CHAT>: No data to be received.")
            break
        if "&&&&" not in message:
            if message != "":
                message_to_send = username + "%" + message
                # Uses send_messages_all function to send message to all clients
                send_messages_all(message_to_send)
                # Tries to open a file with a list of words and check message against it
                # Set doesn't keep duplicates and allows intersection to be performed to compare two sets (words in a file and message)
                try:
                    file =  open('Words.txt', "r", encoding="utf-8")
                    contentsFile = set(file.read().split())
                    messageWords = set(message.split())
                    # If there is a match, user is prompted with a quote
                    if messageWords.intersection(contentsFile):
                        textPrompt = username + "! " + random.choice(promptQuotes)
                        message_prompt_to_send = "CHAT" + "%" +  textPrompt
                        send_messages_all(message_prompt_to_send )
                        file.close()
                    else:
                        pass
                except:
                    print("<CHAT>: no file available.")
            else:
                print(f"<CHAT>: error: No message from {username}")
                break
        else:
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()
            print("Connection closed.")
            break

# Function sends messages to all connected clients.
# Using the send_message_one function and iteration of all connected clients [].
def send_messages_all(message):   
    for user in connected_sockets:
        send_message_one(user[1], message)


# Function to send messages to one unique client:
def send_message_one(client_socket,message):
    try:
        client_socket.sendall(message.encode())
    except:
        print("Error: cannot send a message. ")


main_server()



