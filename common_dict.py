import sys
import socket
import itertools


host = sys.argv[1]
port = int(sys.argv[2])

common_passwords = [
    password.rstrip() for password in list(open("passwords.txt").readlines())]

client_socket = socket.socket()
address = (host, port)

state = False

client_socket.connect(address)

# For each password in list, generate a list of all capitalized and uncapitalized permutations
for password in common_passwords:
    combinations = list(map(lambda x: ''.join(x), itertools.product(
        *([letter.lower(), letter.upper()] for letter in password))))

    # For each combination, send through web socket and get response
    for combination in combinations:
        # SEND TO WEB SOCKET HERE
        print(combination)

client_socket.close()
