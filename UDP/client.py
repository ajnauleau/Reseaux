import socket

params = ('127.0.0.1', 8808)
BUFFER_SIZE = 1024 #default

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b"World", params)

data, _ = s.recvfrom(BUFFER_SIZE)

print('\tData received from server : %s', data)

s.close()