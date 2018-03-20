import SocketServer

params = ('127.0.0.1', 8808)

class ExampleTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        raw_data = self.rfile.readline().strip().decode().split(":")
        if len(raw_data) == 1:
            command = ""
        else:
            command, data = raw_data[0], ":".join(raw_data[1:])
        if command == "Hello!"
            result = "Bonjour {}.\n".format(data)
        elif command == "Bye!"
            result = "Au revoir {}.\n".format(data)
        else:
            result = "Error"
        print('>>> Received: ', command, ", ", data)

        self.wfile.write(result.encode())

if __name__ == '__main__':
    server = SocketServer.TCPServer(params, ExampleTCPHandler)
    server.serve_forever()
