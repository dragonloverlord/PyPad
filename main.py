__author__ = 'dragonloverlord'

from gi.repository import Gtk


class PadWindow(Gtk.Window):
    def __init__(self):
        #window stuff
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)

        #main grid
        self.main_grid = Gtk.Grid()
        self.main_grid.set_hexpand(True)
        self.add(self.main_grid)

        #menubar for main grid
        self.main_grid.menubar = Gtk.MenuBar()
        self.main_grid.menubar.set_hexpand(True)
        self.main_grid.attach(self.main_grid.menubar, 0, 0, 1, 1)

        #file menu item for menubar
        self.main_grid.menubar.file_menu = Gtk.MenuItem(label="File")

        #submenu for file menu
        self.main_grid.menubar.file_menu.submenu = Gtk.Menu()

        #new file menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.new_file = Gtk.MenuItem(label="New File")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.new_file, 0, 1, 0, 1)

        #open file menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.open_file = Gtk.MenuItem(label="Open...")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.open_file, 0, 1, 1, 2)

        #save file menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.save_file = Gtk.MenuItem(label="Save")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.save_file, 0, 1, 2, 3)

        #save as menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.save_as = Gtk.MenuItem(label="Save As...")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.save_as, 0, 1, 3, 4)

        #attachers and settings
        self.main_grid.menubar.file_menu.set_submenu(self.main_grid.menubar.file_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.file_menu)

        #edit menu item for menubar
        self.main_grid.menubar.edit_menu = Gtk.MenuItem(label="Edit")
        self.main_grid.menubar.append(self.main_grid.menubar.edit_menu)

        #options menu item for menubar
        self.main_grid.menubar.options_menu = Gtk.MenuItem(label="Options")
        self.main_grid.menubar.append(self.main_grid.menubar.options_menu)

        #help menu item for menubar
        self.main_grid.menubar.help_menu = Gtk.MenuItem(label="Help")
        self.main_grid.menubar.append(self.main_grid.menubar.help_menu)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)
pad.show_all()
Gtk.main()