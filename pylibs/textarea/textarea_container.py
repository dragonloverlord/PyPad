__author__ = 'dragonloverlord'

from gi.repository import Gtk
from gi.repository import GtkSource


def textarea_container(pad):
    pad.main_grid.textarea_container = Gtk.ScrolledWindow(None, None)

    pad.main_grid.textarea_container.buffer = GtkSource.Buffer()

    pad.main_grid.textarea_container.textarea = Gtk.TextView.new_with_buffer(pad.main_grid.textarea_container.buffer)
    pad.main_grid.textarea_container.textarea.set_hexpand(True)
    pad.main_grid.textarea_container.textarea.set_vexpand(True)
    pad.main_grid.textarea_container.textarea.set_wrap_mode(Gtk.WrapMode.WORD)
    pad.main_grid.textarea_container.add_with_viewport(pad.main_grid.textarea_container.textarea)

    pad.main_grid.textarea_container.set_hexpand(True)
    pad.main_grid.textarea_container.set_vexpand(True)
    pad.main_grid.attach(pad.main_grid.textarea_container, 0, 1, 1, 1)
