import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Graphic.Direction.client import set_ihm

set_ihm(Gtk.Builder(), "client")