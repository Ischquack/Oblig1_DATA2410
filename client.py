import socket
import threading
import time
import bot

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.176"
ADDR = (SERVER, PORT)

nickname = input('Choose a nickname: ')
if nickname in bot.bots:
    nickname.start()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                'if message contains' 
                print(message)

        except:
            print('An error occured')
            client.close()
            break

def write():
    while True:
        time.sleep(1)
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