import socketserver

params = ('127.0.0.1', 8808)

class ExampleTCPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        print('>>> Received: %s', data)
        self.wfile.write(b"Hello " + data.strip() + b". \n")

if __name__ == '__main__':
    server = socketserver.UDPServer(params, ExampleTCPHandler)
    server.serve_forever()


