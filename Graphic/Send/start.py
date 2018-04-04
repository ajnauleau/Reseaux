import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Graphic.Send.client import set_code

set_code(Gtk.Builder(), "code")