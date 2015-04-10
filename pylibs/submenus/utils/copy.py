__author__ = 'dragonloverlord'

from gi.repository import Gtk
from gi.repository import Gdk


global pad

def set_pad_copy(pad_two):
    global pad

    pad = pad_two

def copy(menuitem):
    clipboard = pad.main_grid.textarea_container.textarea.get_clipboard(Gdk.Atom.intern("CLIPBOARD", True))
    pad.main_grid.textarea_container.buffer.copy_clipboard(clipboard)
