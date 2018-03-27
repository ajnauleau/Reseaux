import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


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
            result.set_text(value)
        else:
            result.set_text('')


builder = Gtk.Builder()
builder.add_from_file("/Users/Antoine/Developer/Code/Python/Glade/hello.glade")
builder.connect_signals(Handler(builder))

if __name__ == "__main__":
    window = builder.get_object("principle_window")
    window.show_all()

    Gtk.main()


