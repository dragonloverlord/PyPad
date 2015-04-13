__author__ = 'dragonloverlord'

from gi.repository import Gtk


global pad


def set_pad_redo(pad_two):
    global pad

    pad = pad_two


def redo(menuitem):
    global pad

    pad.main_grid.textarea_container.buffer.redo()