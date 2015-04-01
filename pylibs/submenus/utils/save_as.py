__author__ = 'dragonloverlord'

from gi.repository import Gtk


global pad

def set_pad_save_as(pad_two):
    global pad

    pad = pad_two

def save_as(menuitem):
    def close_dialog(button):
        pad.main_grid.save_as_dialog.close()

    pad.main_grid.save_as_dialog = Gtk.FileChooserDialog()

    pad.main_grid.save_as_dialog.close_button = pad.main_grid.save_as_dialog.add_button("Close", Gtk.ResponseType.CLOSE)
    pad.main_grid.save_as_dialog.close_button.connect("clicked", close_dialog)

    pad.main_grid.save_as_dialog.run()