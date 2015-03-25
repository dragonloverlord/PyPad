__author__ = 'dragonloverlord'

from gi.repository import Gtk


class PadWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)

        self.main_grid = Gtk.Grid()
        self.main_grid.set_hexpand(True)
        self.add(self.main_grid)

        self.main_grid.menubar = Gtk.MenuBar()
        self.main_grid.menubar.set_hexpand(True)
        self.main_grid.attach(self.main_grid.menubar, 0, 0, 1, 1)

        self.main_grid.menubar.file_menu = Gtk.MenuItem(label="File")
        self.main_grid.menubar.file_menu.submenu = Gtk.Menu()
        self.main_grid.menubar.file_menu.submenu.new_file = Gtk.MenuItem(label="New File")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.new_file, 0, 1, 0, 1)
        self.main_grid.menubar.file_menu.set_submenu(self.main_grid.menubar.file_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.file_menu)

        self.main_grid.menubar.edit_menu = Gtk.MenuItem(label="Edit")
        self.main_grid.menubar.append(self.main_grid.menubar.edit_menu)

        self.main_grid.menubar.options_menu = Gtk.MenuItem(label="Options")
        self.main_grid.menubar.append(self.main_grid.menubar.options_menu)

        self.main_grid.menubar.help_menu = Gtk.MenuItem(label="Help")
        self.main_grid.menubar.append(self.main_grid.menubar.help_menu)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)
pad.show_all()
Gtk.main()