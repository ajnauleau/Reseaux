#!/usr/local/bin/python
import socket
import json
import gi
import zlib
import base64
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

params = ('127.0.0.1', 8808)

BUFFER_SIZE = 1024

def set_code(builder, code_name):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(params)
        s.send("load_code:{}\n".format(code_name).encode())
        result = b""
        while True:
            res = s.recv(BUFFER_SIZE)
            if not res:
                break
            result += res

        code = zlib.decompress(base64.b64decode(result))

        d = locals()
        exec(code, d, d)

        Handler = d["Handler"]
        builder.add_from_file("/Users/Antoine/Developer/Code/Python/Reseaux/Glade/hello.glade")
        builder.connect_signals(Handler(builder))

        print(Handler(builder))

        window = builder.get_object("principle_window")
        window.show_all()

        Gtk.main()

