# Learn To Debate chat tool - LDCT - CLIENT SIDE - LOCAL
# VS MSc IT Birkbeck 2023
# -------------------------------

# Summary:
# This is a client side of the program that runs along with the server side that is run first.
# It has three frames.

# Frame 1 - Info
# The first frame user sees. It has About, Report Issue, Start a Chat buttons, and a picture.
# Start a Chat button moves user to the next frame.

# Frame 2 - Chat
# Here user provides a username and IP address in the entry box.
# Once provided, the client connects to the server that is already running.
# If connection is successful, user chats to other connected clients.
# Once chat is finished, user clicks End Chat button, and moves to third frame.

# Frame 3 - Feedback & Save chat
# While users were chatting, the program created a txt file and wrote into it contents of the chat.
# In frame 3, user can add optional feedback and click Save Chat button.
# There is also an inspirational quote displayed at the bottom of the frame.
# The quote is randomly selected from the list of quotes.

# Imports
import random
import socket
import threading
from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime
import random
from PIL import ImageTk, Image
import os 

# Changing working directory of Python to where the script is located, to enable file opening
os.chdir(os.path.dirname(__file__))
# print("THIS IS DIRECTORY" + os.getcwd()) # Test

# tkinter._test() # Test

# Random quotes to be displayed at the end
quotes = ["~ Those who cannot change their minds cannot change anything. ~ \n George Bernard Shaw",
"~ Don't raise your voice, improve your argument. ~ \n Desmond Tutu",
"~ Those who cannot understand how to put their thoughts on ice,\n should not enter into the heat of debate. ~ \n Friedrich Nietzsche",
"~ For good ideas and true innovation, you need human interaction,\n conflict, argument, debate. ~ \n Margaret Heffernan",
"~ You aren't mature enough to debate something - \n if you can't accept the possibility of being wrong. ~ \n Ed Latimore ",
"~ Without debate, without criticism, no administration and no country can succeed,\n and no republic can survive. ~ \n John F. Kennedy",
"~ If you only read the books that everyone else is reading,\n you can only think what everyone else is thinking. ~ \n Haruki Murakami ",
"~ Time spent arguing is, oddly enough, almost never wasted. ~ \n Christopher Hitchens",
"~ When the debate is lost, slander becomes the tool of the loser. ~ \n Socrates "]

# Colours 
PURPLE_COL = "#5D478B"
PURPLE_COL_l = "#E6E6FA"
WHITESMOKE_COL = "#F5F5F5"
OLIVE_COL = "#556B2F"
YELLOW_COL = "#EEC900"
FONT = "Arial"
FONT_IT = "Arial italic"

# Client socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connection details
# HOST =  "***" # IPV4 public address of the server, for the connection via Internet
# HOST to connect is located in the join_chat function, and it is entered by user in IP_entry
PORT = 12345

# Text file where Chat is saved
# Unique file name generated with datetime module
try:
    filename = str(datetime.datetime.now().strftime("%Y:%m:%d:%H:%M")).replace(':', '.')
    file_txt = open(f"Learn To Debate Chat {filename}.txt", "w")
    file_txt.close()
except:
    print("Error creating file.")


# Widgets and functions - first frame
def add_widgets_frame_one():
    
    # Functions - first frame
    # Function to display text when info button is clicked
    def frame_one_show_about():
        show_info_text = tk.Label(inner_frame_top,
            text="It is a tool that can be used to master debate skills and critical thinking.\n"
            "It allows you to chat with an opponent and to save your chat as a text file. \n"
            "Click “Report an issue” if the tool does not work. \n"
            "Happy chatting!", fg="black", bg=WHITESMOKE_COL, font=(FONT_IT, 10))
        show_info_text.pack()
        window.after(10000, frame_one_remove_about, show_info_text)

    # Function to remove text of info button after 10 sec
    def frame_one_remove_about(widget):
        widget.destroy()

    # Function to display text when report button is clicked
    def frame_one_report_msg():
        show_report_msg = tk.Label(inner_frame_top,
            text="Sorry the chat does not work as it should.\n"
            "Please send screenshots and comments to:\n"
            "***@gmail.com",
            fg="black", bg=WHITESMOKE_COL, font=(FONT_IT, 10))
        show_report_msg.pack()
        window.after(10000, frame_one_remove_report_msg, show_report_msg)

    # Function to remove text of report button after 10 sec
    def frame_one_remove_report_msg(widget):
        widget.destroy()

    # First frame has three inner frames (Top, Middle, Bottom) to position multiple widgets.
    # Top frame
    inner_frame_top = Frame(first_frame_info, bg=WHITESMOKE_COL, width=600, height=70)
    inner_frame_top.pack(fill="x")

    # Middle frame
    inner_frame_mid = Frame(first_frame_info, bg=WHITESMOKE_COL, width=600, height=180)
    inner_frame_mid.pack(fill="x")

    # Bottom frame
    inner_frame_down = Frame(first_frame_info, bg=WHITESMOKE_COL, width=600, height=320)
    inner_frame_down.pack(fill="x")

    # First frame widgets
    # About button displays information when clicked and disappears in 10 sec
    about_text = tk.Button(inner_frame_top,
        text="About the tool", font=(FONT, 11, "bold"),
        fg="white", bg=OLIVE_COL, height=2, width=26,
        command=frame_one_show_about)
    about_text.pack(padx=25, pady=7, side=tk.TOP)

    # Report issue button displays info when clicked and disappears in 10 sec
    report_issue = tk.Button(inner_frame_top,
        text="Report an issue", font=(FONT, 11, "bold"),
        fg="black", bg=YELLOW_COL, height=2, width=26,
        command=frame_one_report_msg)
    report_issue.pack(padx=25, pady=7, side=tk.TOP)

    # Start chat button takes user to the next frame / page.
    start_chat = tk.Button(inner_frame_mid,
        text="Start a Chat", font=(FONT, 15, "bold"),
        fg="white", bg=PURPLE_COL, height=3, width=18,
        command=call_frame_two_chat)
    start_chat.pack(padx=20, pady=7, side=tk.TOP)

    # Picture front page
    path = "deb.PNG"
    try:
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(inner_frame_down, image=img)
        panel.photo = img
        panel.pack(padx=1, pady=5, side=tk.TOP)
    except:
        print("Unable to load image.")

    # General info label
    info_text = tk.Label(inner_frame_down, text="'Learn To Debate chat tool' (c) 2023", bg=WHITESMOKE_COL)
    info_text.pack(padx=1, pady=5, side=tk.BOTTOM)


# Widgets and functions - second frame
def add_widgets_frame_two():
    # Functions - second frame

    # Function to end chat. Sends specific message (&&&&) to server and stops connection.
    # Notifies other users that client has closed the chat.
    # Disables user message_entry & send_boxes for the client that ended the chat.
    def stop_chat():
        try:
            client_socket.send(bytes("I have now closed my chat. To save it correctly and add feedback, end your chat and go to the next screen.", "utf-8"))
            client_socket.send(bytes("&&&&", "utf-8"))
            enter_text.config(state=tk.DISABLED)
            send_text.config(state=tk.DISABLED)
            print("stops chat")
        except:
            OSError

    # Function to join the chat.
    # Will only connect if username and Host / IP is provided.
    # Once connection established, username, IP entry and connect buttons are disabled.
    # Function also starts a thread - listening_to_server.
    # User is also provided with information how to end chat.
    # If connection successful, End Chat button is enabled.
    def join_chat():
        username = username_entry.get()
        HOST = IP_entry.get()
        if username != "" and HOST != "":
            username_entry.configure(state=tk.DISABLED)
            username_connect.config(state=tk.DISABLED)
            IP_entry.configure(state=tk.DISABLED)
            try:
                client_socket.connect((HOST, PORT))
                end_chat.config(state=tk.NORMAL)
                chat_box.config(state=tk.NORMAL)
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: Success. You are connected to the server.' + '\n')
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: The chat will be saved as a text file in your folder.' + '\n')
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: To finish, click "End Chat" to save it correctly and add feedback on the next screen.' + '\n')
                chat_box.config(state=tk.DISABLED)
                client_socket.sendall(username.encode('utf-8'))
            except OSError as error:
                print(error)
                chat_box.config(state=tk.NORMAL)
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: System error. You are not connected to the server. Check your connection and restart the chat.' + '\n')
                chat_box.config(state=tk.DISABLED)
            except Exception as error:
                print(error)
                chat_box.config(state=tk.NORMAL)
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: You are not connected to the server. Check your connection and restart the chat.' + '\n')
                chat_box.config(state=tk.DISABLED)
        else:
            chat_box.config(state=tk.NORMAL)
            chat_box.insert("1.0","<CHAT>: Username or IP address is empty. Try again." + '\n')
            chat_box.config(state=tk.DISABLED)

        threading.Thread(target=listening_to_server, args=(client_socket,)).start()

    # Function to send a message that user has entered from enter_text box to server, or to display error.
    # It gets message from enter_text box and then deletes text from it, ready for new message.
    def send_msg():
        msg = enter_text.get()
        #print(msg)
        if msg != "":
            try:
                client_socket.sendall(msg.encode('utf-8'))
                enter_text.delete(0,len(msg))
            except:
                chat_box.config(state=tk.NORMAL)
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: You are not connected.' + '\n')
                chat_box.config(state=tk.DISABLED)
        else:
            chat_box.config(state=tk.NORMAL)
            chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: Empty message.' + '\n')
            chat_box.config(state=tk.DISABLED)

    # Function to listen for incoming messages from server & decode them.
    # Message is displayed to all connected clients, and also written into a text file.
    def listening_to_server(client_socket):
        while 1:
            try:
                msg = client_socket.recv(1024).decode("utf-8")
            except:
                print("<CHAT>: error in receiving the message from the server, encoding it, or connection issue.")
                break
            if msg != "":
                username = msg.split("%")[0]
                content = msg.split("%")[1]
                # Writing the received message into a file
                file_txt = open(f"Learn To Debate chat {filename}.txt", "a", encoding="utf-8")
                file_txt.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} <{username}>: {content}\n')
                file_txt.close()
                # Displaying the received message for user
                chat_box.config(state=tk.NORMAL)
                chat_box.insert("1.0", f'{datetime.datetime.now().strftime("%H:%M:%S")} <{username}>: {content}\n')
                chat_box.config(state=tk.DISABLED)
                # Displaying no message error
            else:
                chat_box.config(state=tk.NORMAL)
                chat_box.insert("1.0",f'{datetime.datetime.now().strftime("%H:%M:%S")} <CHAT>: No more messages received.' + '\n')
                chat_box.config(state=tk.DISABLED)
                break

    # Second frame has three inner frames (Top, Middle, Bottom) to position of multiple widgets.
    # Top frame
    inner_frame_top = Frame(frame_two_chat, bg=PURPLE_COL_l, width=600, height=60)
    inner_frame_top.pack()

    # Middle frame
    inner_frame_mid = Frame(frame_two_chat, bg=PURPLE_COL_l, width=600, height=350)
    inner_frame_mid.pack(fill="x")

    # Bottom frame
    inner_frame_down = Frame(frame_two_chat, bg=PURPLE_COL, width=600, height=87)
    inner_frame_down.pack(fill="x")

    # Widgets in Top Frame (Second frame)
    # Username entry with placeholder text
    username_entry = ctk.CTkEntry(inner_frame_top,
            validate="focusout", width=150, height=7,
            font=(FONT_IT, 10), placeholder_text="Enter username..")
    username_entry.pack(side=tk.LEFT, padx=5, pady=5)
    username_entry.configure(state=tk.NORMAL)

    # IP address of the server to connect to, user has to provide where they are connecting the client
    IP_entry = ctk.CTkEntry(inner_frame_top,
            validate="focusout", width=150, height=7,
            font=(FONT_IT, 10), placeholder_text="Enter server IP..")
    IP_entry.pack(side=tk.LEFT, padx=5, pady=5)
    IP_entry.configure(state=tk.NORMAL)

    # Join chat button, calls join_chat function defined above
    username_connect = tk.Button(inner_frame_top,
            text="Click to join",
            font=(FONT,10, "bold"),
            fg="white", bg=PURPLE_COL,
            command=join_chat)
    username_connect.pack(side=tk.LEFT, padx=5, pady=5)
    username_connect.config(state=tk.NORMAL)

    # Back button, allows user to go back to the first screen (e.g. if they need to check how to report errors)
    back_button = tk.Button(inner_frame_top,
            text="Back", font=(FONT,10, "bold"),
            bg=PURPLE_COL_l,
            command=call_frame_one)
    back_button.pack(side=tk.LEFT, padx=5, pady=5)

    # End chat button
    # The button is disabled until there is an established connection.
    # Will do several things at a time: will end chat (by calling stop_chat function),
    # Close text file, and move user to the third last frame.
    # Command: lambda is used to have multiple functions / commands for 1 button. 
    end_chat = tk.Button(inner_frame_top, text="End chat", font=(FONT,10, "bold"),
                         bg=OLIVE_COL, fg="White", command=lambda:[stop_chat(),call_frame_three()])
    end_chat.pack(side=tk.LEFT, padx=5, pady=5)
    end_chat.config(state=tk.DISABLED)

    # Widgets in middle frame (Second frame)
    # Chat display
    # User will not be able to type, but chat messages will be displayed in it.
    chat_box = scrolledtext.ScrolledText(inner_frame_mid, state=tk.DISABLED,
                                         borderwidth=5, relief="groove")
    chat_box.pack(side=tk.LEFT, padx=3, pady=3)

    # Widgets in bottom frame (Second frame)
    # Message entry for users chat messages
    enter_text = tk.Entry(inner_frame_down, validate="focusout",
                          width=70, font=(FONT_IT, 10))
    enter_text.pack(side=tk.LEFT, padx=5, pady=20)

    # Send button to send messages, calls send_msg function
    send_text = tk.Button(inner_frame_down, text="Send",font=(FONT,10, "bold"),
                                         bg=PURPLE_COL_l, command=send_msg)
    send_text.pack(side=tk.LEFT, padx=5, pady=20)

# Widgets and functions - third frame:
def add_widgets_frame_three():

# Functions - third frame
# Function delete_repetition is called when user clicks Save button.
# It deletes identical lines (if any) from the text file.
# These repetitions may occur when server sends one message to several connected clients,
# So same message is written into the text file multiple times.
# Function creates a temporary list, iterates over text file, adds to the list lines that don't repeat, and corrects the file by overwriting it.
    def delete_repetition():
        file_txt = open(f"Learn To Debate chat {filename}.txt","r")
        list_txt = []
        for i in file_txt:
            if i not in list_txt:
                list_txt.append(i)
        file_txt.close()
        file_txt = open(f"Learn To Debate chat {filename}.txt","w")
        for j in list_txt:
            file_txt.write(j)
        file_txt.close()

    # Function that captures feedback text (if any) from the feedback window, and adds it into the text file.
    # If no text in the feedback window provided, it just calls the delete_repetition function that corrects the file.
    def save_n_close():
        feedback_text = feedback_window.get('1.0', tk.END)
        if feedback_text != "":
            file_txt = open(f"Learn To Debate chat {filename}.txt","a")
            file_txt.write(f"Addional feedback: {feedback_text} \n")
            file_txt.close()
        else:
            pass
        delete_repetition()
        close_now()

    # Function to display goodbye text when Save chat button is clicked.
    # It also empties and disables the feedback window.
    def close_now():
        feedback_window.delete('1.0', END)
        feedback_window.insert("1.0", f'Your feedback, if any, was written into the file.')
        feedback_window.config(state=tk.DISABLED)
        close_now_text = tk.Label(frame_three,
            text="You can now close the program.\n"
            "Thanks for chatting!", fg="black", bg=YELLOW_COL, font=(FONT, 10))
        close_now_text.pack()
   

    # Widgets in frame three
    # Label for the feedback window
    feedback_label = tk.Label(frame_three, text="Optional additional feedback",
        font=("Arial bold", 10),
        bg=WHITESMOKE_COL, width=50, height=1)
    feedback_label.pack(side=tk.TOP, padx=5, pady=6)

    # Feedback window
    feedback_window = scrolledtext.ScrolledText(frame_three, state=tk.NORMAL,
        borderwidth=2, relief="groove", width=50,
    height=10)
    feedback_window.pack(side=tk.TOP, padx=5, pady=5)

    # Button to Save chat. It takes input from feedback window and runs save_n_close function.
    save_chat = tk.Button(frame_three, text="Save chat", font=(FONT,10, "bold"),
                         bg=OLIVE_COL, fg="White", command=save_n_close)
    save_chat.pack(side=tk.TOP, padx=5, pady=5)

    # Back button left for testing. It allows to go back to second frame from third frame.
    # back_button = tk.Button(frame_three,
    #                                      text="Back", font=(FONT,10, "bold"),
    #                                      bg=PURPLE_COL_l,
    #                                       command=call_frame_two_from_three)
    # back_button.pack(side=tk.TOP, padx=5, pady=5)

    # Random quote at the end, text label
    quote_arg = ctk.CTkLabel(frame_three, font=(FONT_IT, 13), text=random.choice(quotes),
        width=400, height=50)
    quote_arg.pack(side=tk.BOTTOM, padx=10, pady=50)



# General functions
# Functions to move between three main frames. They make one to be hidden, and another appear.
# Will call the second frame to appear, and first to close.
def call_frame_two_chat():
    first_frame_info.pack_forget()
    frame_two_chat.pack()

# Will call second frame to appear, and third to close (e.g. if back button is clicked).
# Can be used for testing.
def call_frame_two_from_three():
    frame_three.pack_forget()
    frame_two_chat.pack()

# Will call the third frame to appear, and second to close.
def call_frame_three():
    frame_two_chat.pack_forget()
    frame_three.pack()

# Will call the first frame to appear, and second to close. (e.g. if back button is clicked).
def call_frame_one():
    frame_two_chat.pack_forget()
    first_frame_info.pack()

### Window - main window of the LDCT ###
window = tk.Tk()

# Setting window title and size
window.title("Learn To Debate chat tool")
window.geometry("600x500")
window.configure(background=WHITESMOKE_COL)
window.resizable(False, False) 

# Frames inside main window that will have all other elements in them.
first_frame_info=Frame(window, bg=WHITESMOKE_COL)
first_frame_info.pack()
frame_two_chat= Frame(window, bg=PURPLE_COL_l)
frame_two_chat.pack()
frame_three= Frame(window, bg=WHITESMOKE_COL)
frame_three.pack()

# Functions to add all widgets to all three frames
add_widgets_frame_one()
add_widgets_frame_two()
add_widgets_frame_three()

# Hide frames, but leave first frame visible,
# So they are not all shown at the same time when program launches.
frame_two_chat.pack_forget()
frame_three.pack_forget()

window.mainloop()