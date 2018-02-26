import socket

params = ('127.0.0.1', 8808)
BUFFER_SIZE = 1024 #default

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(params)
    s.listen(1)

    conn, addr = s.accept()
    print('Connection Accepted: %s' % str(addr))

    with conn:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            conn.send(b'Hello ' + data.strip() + b'.\n')
            
