__author__ = 'dragonloverlord'

from gi.repository import Gtk


def options_menu(pad):
    pad.main_grid.menubar.options_menu = Gtk.MenuItem(label="Options")

    pad.main_grid.menubar.options_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

    pad.main_grid.menubar.options_menu.submenu.font_options = Gtk.MenuItem(label="Font")
    pad.main_grid.menubar.options_menu.submenu.attach(pad.main_grid.menubar.options_menu.submenu.font_options, 0, 1, 0,
                                                      1)

    pad.main_grid.menubar.options_menu.submenu.word_wrap_options = Gtk.MenuItem(label="Word Wrap")
    pad.main_grid.menubar.options_menu.submenu.attach(pad.main_grid.menubar.options_menu.submenu.word_wrap_options, 0,
                                                      1, 1, 2)

    pad.main_grid.menubar.options_menu.set_submenu(pad.main_grid.menubar.options_menu.submenu)
    pad.main_grid.menubar.append(pad.main_grid.menubar.options_menu)
