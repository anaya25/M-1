
import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}


def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

def setup():
    print("\n\n\n\n\n\n\n FTP MESSSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    #CONNECTIONS
    SERVER.listen(100)

    print("\t\t\t\t\t SERVER IS WAITING FOR INCOMING CONNECTION...")
    print("\n")
    
    acceptConnections()

#receiving multiple messages
setup_thread = Thread(target=setup)
setup_thread.start()
