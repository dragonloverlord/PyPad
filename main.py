__author__ = 'dragonloverlord'

from gi.repository import Gtk

class PadWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)
pad.show_all()
Gtk.main()