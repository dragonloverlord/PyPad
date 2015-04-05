__author__ = 'dragonloverlord'

from gi.repository import Gtk
from .utils.save_as import save_as
from .utils.save_as import set_pad_save_as
from .utils.open_file import open_file
from .utils.open_file import set_pad_open_file


def file_menu(pad):
    set_pad_save_as(pad)
    set_pad_open_file(pad)

    pad.main_grid.menubar.file_menu = Gtk.MenuItem(label="File")

    pad.main_grid.menubar.file_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

    pad.main_grid.menubar.file_menu.submenu.new_file = Gtk.MenuItem(label="New File")
    pad.main_grid.menubar.file_menu.submenu.attach(pad.main_grid.menubar.file_menu.submenu.new_file, 0, 1, 0, 1)

    pad.main_grid.menubar.file_menu.submenu.open_file = Gtk.MenuItem(label="Open...")
    pad.main_grid.menubar.file_menu.submenu.open_file.connect("activate", open_file)
    pad.main_grid.menubar.file_menu.submenu.attach(pad.main_grid.menubar.file_menu.submenu.open_file, 0, 1, 1, 2)

    pad.main_grid.menubar.file_menu.submenu.save_file = Gtk.MenuItem(label="Save")
    pad.main_grid.menubar.file_menu.submenu.attach(pad.main_grid.menubar.file_menu.submenu.save_file, 0, 1, 2, 3)

    pad.main_grid.menubar.file_menu.submenu.save_as = Gtk.MenuItem(label="Save As...")
    pad.main_grid.menubar.file_menu.submenu.save_as.connect("activate", save_as)
    pad.main_grid.menubar.file_menu.submenu.attach(pad.main_grid.menubar.file_menu.submenu.save_as, 0, 1, 3, 4)

    pad.main_grid.menubar.file_menu.submenu.separator_menu_item = Gtk.SeparatorMenuItem()
    pad.main_grid.menubar.file_menu.submenu.attach(pad.main_grid.menubar.file_menu.submenu.separator_menu_item, 0, 1, 4,
                                                   5)

    pad.main_grid.menubar.file_menu.submenu.quit_pypad = Gtk.MenuItem(label="Quit")
    pad.main_grid.menubar.file_menu.submenu.quit_pypad.connect("activate", Gtk.main_quit)
    pad.main_grid.menubar.file_menu.submenu.attach(pad.main_grid.menubar.file_menu.submenu.quit_pypad, 0, 1, 5, 6)

    pad.main_grid.menubar.file_menu.set_submenu(pad.main_grid.menubar.file_menu.submenu)
    pad.main_grid.menubar.append(pad.main_grid.menubar.file_menu)