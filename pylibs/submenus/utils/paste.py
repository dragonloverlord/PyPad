__author__ = 'dragonloverlord'

from gi.repository import Gtk


global pad

def set_pad_paste(pad_two):
    global pad

    pad = pad_two

def paste(menuitem):
    pad.main_grid.textarea_container.textarea.do_paste_clipboard()
