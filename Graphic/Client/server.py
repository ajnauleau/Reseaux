import SocketServer
import json

params = ('127.0.0.1', 8808)

class ExampleTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        raw_data = json.loads(self.rfile.readline().strip().decode())
        print('>>> Received: ', raw_data)
        command, data = raw_data.get("command", ""), raw_data.get("message", "")
        if command == "Hello!":
            result = "Bonjour {}.\n".format(data)
        elif command == "Bye!":
            result = "Au revoir {}.\n".format(data)
        else:
            result = "Error"
        print('>>> Received: ', command, ", ", data)

        self.wfile.write(result.encode())

if __name__ == '__main__':
    server = SocketServer.TCPServer(params, ExampleTCPHandler)
    server.serve_forever()
