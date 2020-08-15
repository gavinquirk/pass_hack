import sys
import socket
import itertools


characters = list('abcdefghijklmnopqrstuvwxyz0123456789')

ip = sys.argv[1]
port = int(sys.argv[2])

password = ''


# 1 Create a new socket and connect to host
web_socket = socket.socket()
web_socket.connect((ip, port))

# 2 Generate possible password, encode and send
for character in range(0, len(characters) + 1):
    for combination in itertools.combinations(characters, character):
        # web_socket.send(combination.encode())
        # response = web_socket.recv(1024).decode()
        # print(response)
        print(combination)


web_socket.close()
