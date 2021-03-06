import socket
import threading
import time
import bot

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = 'localhost'
ADDR = (SERVER, PORT)

nickname = input('Choose a nickname: ')
action = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            elif message.startswith("#ACTION"):
                message = message.replace("#ACTION", "")
                action = message
            elif message.startswith("#SUGGESTION"):
                message = message.replace("#SUGGESTION", "") 
                print(message)
                response = bot.selectBot(nickname, action)
                client.send(f"{nickname}: {response}".encode(FORMAT))
                print("You: " + response)
            elif message.startswith("#USERINPUT"):
                print(message)
            else: print(message)

        except:
            print('An error occured')
            client.shutdown()
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

'''
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello Døske!")
input()
send("HEIHIEIIEI")
input()
send(DISCONNECT_MESSAGE)
'''