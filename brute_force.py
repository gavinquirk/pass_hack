import sys
import socket
import itertools


host = sys.argv[1]
port = int(sys.argv[2])
characters = list('abcdefghijklmnopqrstuvwxyz0123456789')
client_socket = socket.socket()
address = (host, port)
client_socket.connect(address)
state = False

for i in range(1, len(characters) + 1):
    for combination in itertools.product(characters, repeat=i):
        password = "".join(combination)
        client_socket.send(password.encode())
        response = client_socket.recv(1024).decode()
        if response == "Connection success!":
            print(password)
            state = True
            break
    if state:
        break

client_socket.close()
