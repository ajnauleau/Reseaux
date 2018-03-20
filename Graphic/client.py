import socket
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

params = ('127.0.0.1', 8808)

BUFFER_SIZE = 1024

def getresult(value):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect(params)
        s.send("{}\n".format(value).encode())
        result = s.recv(BUFFER_SIZE)

        print('\tData from server : {}'.format(result))
        return result.decode()