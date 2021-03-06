import random
import socket
import threading
import story
import time

HEADER = 64
PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print('Server is listening for connections..')

clients = []
nicknames = []


def broadcast(message, compare):
    for client in clients:
        if client != compare:
            #time.sleep(0.2)
            client.send(message.encode(FORMAT))
        
def sendSuggestion():
    action = random.choice(story.actions)
    actionMsg = "#ACTION" + action
    broadcast(actionMsg, None)
    question = random.choice(story.suggestions).format(action)
    message = "#SUGGESTION{} \n".format(question)
    broadcast(message, None)


def handle(client):
    if len(clients) > 0:
        #time.sleep(1.1)
        sendSuggestion()
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            #client.shutdown()
            client.close()
            #time.sleep(1)
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            nickname = nicknames[index]
            broadcast(f'{nickname}: left the chat', None)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname} \n')
        broadcast(f'{nickname} has entered the chat \n', client)
        client.send('Connected to the server'.encode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

receive()


'''
def handle_client(client):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting..")
start()
'''