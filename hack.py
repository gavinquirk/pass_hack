import sys
import socket

ip = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]

# 1 Create a new socket.
my_socket = socket.socket()

# 2 Connect to a host and a port using the socket.
my_socket.connect((ip, port))

# 3 Send a message from the third command line argument to the host using the socket.
my_socket.send(message.encode())

# 4 Receive the server’s response.
response = my_socket.recv(1024).decode()

# 5 Print the server’s response.
print(response)

# 6 Close the socket.
my_socket.close()
