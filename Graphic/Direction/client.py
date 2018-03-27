#!/usr/local/bin/python
import socket
import json
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

params = ('127.0.0.1', 8808)

BUFFER_SIZE = 1024

def set_ihm(builder, ihm_name):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(params)
        s.send("load_file:{}\n".format(ihm_name).encode())
        result = b""
        while True:
            res = s.recv(BUFFER_SIZE)
            if not res:
                break
            result += res
        builder.add_from_string(result.decode())
        print(result.decode())

