__author__ = 'dragonloverlord'

from gi.repository import Gtk

class PadWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)

        self.main_grid = Gtk.Grid()
        self.main_grid.set_hexpand = True
        self.add(self.main_grid)

        self.main_grid.menubar = Gtk.MenuBar()
        self.main_grid.menubar.set_hexpand = True
        self.main_grid.attach(self.main_grid.menubar, 0, 0, 1, 1)

        self.main_grid.menubar.file_menu = Gtk.MenuItem(label="File")
        self.main_grid.menubar.append(self.main_grid.menubar.file_menu)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)
pad.show_all()
Gtk.main()