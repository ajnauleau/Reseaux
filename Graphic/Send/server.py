#!/usr/local/bin/python
import SocketServer
import json
import zlib
import base64

params = ('127.0.0.1', 8808)

class ExampleTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):

        raw_data = self.rfile.readline().strip().decode().split(":")
        print('>>> Received: ', raw_data)

        command, data = raw_data[0], raw_data[1]

        if command == "load_file":
            with open("/Users/Antoine/Developer/Code/Python/Reseaux/Glade/{}.glade".format(data), "rb") as f:
                self.wfile.write(f.read())
        elif command == "load_code":
            with open("/Users/Antoine/Developer/Code/Python/Reseaux/Graphic/Send/{}.py".format(data), "rb") as f:
                self.wfile.write(base64.b64encode(zlib.compress(f.read())))


if __name__ == '__main__':
    server = SocketServer.TCPServer(params, ExampleTCPHandler)
    server.serve_forever()
