__author__ = 'dragonloverlord'

from gi.repository import Gtk


global pad


def set_pad_undo(pad_two):
    global pad

    pad = pad_two


def undo(menuitem):
    global pad

    pad.main_grid.textarea_container.buffer.undo()