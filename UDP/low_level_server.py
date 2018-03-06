import socket

params = ('127.0.0.1', 8808)
BUFFER_SIZE = 1024 #default

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(params)

data, addr = s.recvfrom(BUFFER_SIZE)

print(">>> Received: ", data, "from:", addr)

s.sendto(b"Hello " + data.strip() + b".\n", addr)

s.close()