__author__ = 'dragonloverlord'

from gi.repository import Gtk

def main_grid(pad):
    pad.main_grid = Gtk.Grid()
    pad.main_grid.set_hexpand(True)
    pad.add(pad.main_grid)