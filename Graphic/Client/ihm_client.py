import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Graphic.Client.client import get_result

class Handler:

    def __init__(self, builder):

        self.builder = builder

    def on_principle_window_delete_event(self, widget, event):

        print("Bye.")
        Gtk.main_quit(widget, event)

    def on_hello_button_clicked(self, button):

        print("Hello World!")
        entry = self.builder.get_object('entry')
        result = self.builder.get_object('result')
        value = entry.get_text()

        if value:
            result.set_text(get_result("Hello!", value))
        else:
            result.set_text('')

    def on_bye_button_clicked(self, button):

        print("Bye World!")
        entry = self.builder.get_object('entry')
        result = self.builder.get_object('result')
        value = entry.get_text()

        if value:
            result.set_text(get_result("Bye!", value))
        else:
            result.set_text('')

builder = Gtk.Builder()
builder.add_from_file("/Users/Antoine/Developer/Code/Python/Reseaux/Glade/client.glade")
builder.connect_signals(Handler(builder))

if __name__ == "__main__":
    window = builder.get_object("principle_window")
    window.show_all()

    Gtk.main()


