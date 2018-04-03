#!/usr/local/bin/python
import socket
import json
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

params = ('127.0.0.1', 8808)

BUFFER_SIZE = 1024

global Handler

def get_result(value):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(params)
        s.send("{}\n".format(value).encode())
        result = s.recv(BUFFER_SIZE)
        s.close()

        print('\tData from server : {}'.format(result))
        return result.decode()

