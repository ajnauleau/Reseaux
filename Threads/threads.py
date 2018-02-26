import threading
import SocketServer

PARAMS = ('127.0.0.1', 8808)

class ExampleUDPHandler(SocketServer.DatagramRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()
        data = self.rfile.readline().strip()
        print('>>> Recv: %s', data, ', current thread:', cur_thread)
        self.wfile.write(b"Hello " + data.strip() + b". \n")

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    server = ThreadedTCPServer(PARAMS, ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    input()

    server.shutdown()
    server.serve_close()
    
