__author__ = 'dragonloverlord'

from gi.repository import Gtk


def menubar(pad):
    pad.main_grid.menubar = Gtk.MenuBar()
    pad.main_grid.menubar.set_hexpand(True)
    pad.main_grid.attach(pad.main_grid.menubar, 0, 0, 1, 1)