import SocketServer

params = ('127.0.0.1', 8808)

class ExampleTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        self.wfile.write(b"Hello " + data.strip() + b" .\n")

if __name__ == '__main__':
    server = SocketServer.TCPServer(params, ExampleTCPHandler)
    server.serve_forever()

