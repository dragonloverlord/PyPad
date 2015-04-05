__author__ = 'dragonloverlord'

from gi.repository import Gtk


def help_menu(pad):
    pad.main_grid.menubar.help_menu = Gtk.MenuItem(label="Help")

    pad.main_grid.menubar.help_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

    pad.main_grid.menubar.help_menu.submenu.about_help = Gtk.MenuItem(label="About")
    pad.main_grid.menubar.help_menu.submenu.attach(pad.main_grid.menubar.help_menu.submenu.about_help, 0, 1, 0, 1)

    pad.main_grid.menubar.help_menu.set_submenu(pad.main_grid.menubar.help_menu.submenu)
    pad.main_grid.menubar.append(pad.main_grid.menubar.help_menu)
