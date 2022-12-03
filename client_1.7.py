import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
#var
username="nonameplaceholdertextdummy00000000000000000000000000000"
class var:
    join_msg=" joined"
    debug_usr_name="Client_Test"
    # null is disabled
    # enable is enabled
    debug_enabled="null"
    seperator="<SEP>"
    serverid="Server"
    leave="left"
init()


colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]


client_color = random.choice(colors)

host_ip=input("Enter host IP: ")
host_port=input("Enter host PORT: ")

# server's IP address
# if the server is not on this machine,
# put the private (network) IP address (e.g 192.168.1.2)
#"192.168.1.252:5002"
SERVER_HOST = host_ip
SERVER_PORT = int(host_port)
# server's port
separator_token = var.seperator # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

if var.debug_enabled == "null":
    username = input("Enter name: ")
elif var.debug_enabled == "enable":
    username=var.debug_usr_name

print("[*] Logged in as", username)
print("Colors: Blue, Cyan, Green, Lime, Magenta, Red, Yellow, White, Anything else = Random")
color_input = input("Enter color: ")
if (color_input == "Blue"):
    client_color = Fore.BLUE
elif (color_input == "Cyan"):
    client_color = Fore.CYAN
elif (color_input == "Green"):
    client_color = Fore.GREEN
elif (color_input == "Lime"):
    client_color = Fore.LIGHTGREEN_EX
elif (color_input == "Magenta"):
    client_color = Fore.MAGENTA
elif (color_input == "Red"):
    client_color = Fore.RED
elif (color_input == "Yellow"):
    client_color = Fore.YELLOW
elif (color_input == "White"):
    client_color = Fore.WHITE
elif (color_input != "White"):
    client_color = random.choice(colors)
usr_join_msg = f"{username}{var.join_msg}"
date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
usr_join_msg = f"{client_color}[{date_now}] {var.serverid}{separator_token}{usr_join_msg}{Fore.RESET}\n"
s.send(usr_join_msg.encode())


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send =  input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {username}{separator_token}{to_send}{Fore.RESET}"
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()

