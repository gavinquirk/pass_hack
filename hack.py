import sys
import socket
import itertools


characters = list('abcdefghijklmnopqrstuvwxyz0123456789')

print(characters)

host = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client_socket:
    address = (host, port)
    client_socket.connect(address)

    # 2 Generate possible password, encode and send
    for i in range(1, len(characters) + 1):
        for combination in itertools.product(characters, repeat=i):
            password = "".join(combination)
            client_socket.send(password.encode())
            response = client_socket.recv(1024).decode()
            if response == "Connection success!":
                print(response)
                break

client_socket.close()
