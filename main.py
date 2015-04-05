__author__ = 'dragonloverlord'

from gi.repository import Gtk
from gi.repository import GtkSource
import pylibs


class PadWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)

pylibs.main_grid(pad)
pylibs.menubar(pad)
pylibs.submenus.file_menu(pad)
pylibs.submenus.edit_menu(pad)
pylibs.submenus.options_menu(pad)
pylibs.submenus.help_menu(pad)
pylibs.textarea.textarea_container(pad)

pad.show_all()
Gtk.main()