__author__ = 'dragonloverlord'

from gi.repository import Gtk
from gi.repository import Gdk


global pad

def set_pad_paste(pad_two):
    global pad

    pad = pad_two

def paste(menuitem):
    global pad

    clipboard = pad.main_grid.textarea_container.textarea.get_clipboard(Gdk.Atom.intern("CLIPBOARD", True))
    pad.main_grid.textarea_container.buffer.paste_clipboard(clipboard, None, True)
