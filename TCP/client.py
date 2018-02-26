import socket

params = ('127.0.0.1', 8808)
BUFFER_SIZE = 1024 # default

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(params)
s.send(b"World")

data = s.recv(BUFFER_SIZE)

print("\tData Received from Server : %s" % data)

s.close()