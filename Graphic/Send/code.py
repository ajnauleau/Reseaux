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

class Handler:

    def __init__(self, builder):

        self.builder = builder

    def on_principle_window_delete_event(self, widget, event):

        print("Bye.")
        Gtk.main_quit(widget, event)

    def on_validation_button_clicked(self, button):

        print("Hello World!")
        entry = self.builder.get_object('entry')
        result = self.builder.get_object('result')
        value = entry.get_text()

        if value:
            result.set_text(get_result(value))
        else:
            result.set_text('')
