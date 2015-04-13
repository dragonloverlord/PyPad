__author__ = 'dragonloverlord'

from gi.repository import Gtk


global pad

def set_pad_delete(pad_two):
    global pad

    pad = pad_two

def delete_selection(menuitem):
    global pad

    pad.main_grid.textarea_container.buffer.delete_selection(True, True)
