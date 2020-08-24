import sys
import socket
import itertools


host = sys.argv[1]
port = int(sys.argv[2])

alphabet = 'abcdefghijklmnopqrstuvwxyz'
cap_alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
numbers = '0123456789'
characters = alphabet + cap_alphabet + numbers

client_socket = socket.socket()
address = (host, port)

state = False

client_socket.connect(address)

# Run possible passwords using common password list (passwords.txt), both uppercase and lowercase characters

client_socket.close()
