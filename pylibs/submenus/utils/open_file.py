__author__ = 'dragonloverlord'

from gi.repository import Gtk


global pad

def set_pad_open_file(pad_two):
    global pad

    pad = pad_two

def open_file(menuitem):
    def close_dialog(button):
        pad.main_grid.open_dialog.close()

    pad.main_grid.open_dialog = Gtk.FileChooserDialog()

    pad.main_grid.open_dialog.close_button = pad.main_grid.open_dialog.add_button("Close", Gtk.ResponseType.CLOSE)
    pad.main_grid.open_dialog.close_button.connect("clicked", close_dialog)

    pad.main_grid.open_dialog.run()