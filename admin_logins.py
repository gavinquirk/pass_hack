import sys
import socket
import itertools
import json

host = sys.argv[1]
port = int(sys.argv[2])

common_logins = [
    login.rstrip() for login in
    list(open("F:/code/Password Hacker/Password Hacker/task/hacking/logins.txt").readlines())]

client_socket = socket.socket()
address = (host, port)

state = False

client_socket.connect(address)


def get_login():
    # For every login in the list, send to server as json data with empty password. When response is Wrong Password!
    # return that login.
    try:
        for login in common_logins:
            data = json.dumps({
                "login": login,
                "password": " "
            })
            client_socket.send(data.encode())
            response = json.loads(client_socket.recv(
                1024).decode(encoding='utf-8'))
            if response == {"result": "Wrong password!"}:
                return login
    except Exception:
        print("Exception occurred")


client_socket.close()
