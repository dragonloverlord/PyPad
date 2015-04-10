__author__ = 'dragonloverlord'

from gi.repository import Gtk
from .utils.undo import undo
from .utils.undo import set_pad_undo
from .utils.redo import redo
from .utils.redo import set_pad_redo
from .utils.paste import paste
from .utils.paste import set_pad_paste


def edit_menu(pad):
    set_pad_undo(pad)
    set_pad_redo(pad)
    set_pad_paste(pad)

    pad.main_grid.menubar.edit_menu = Gtk.MenuItem(label="Edit")

    pad.main_grid.menubar.edit_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

    pad.main_grid.menubar.edit_menu.submenu.undo_edit = Gtk.MenuItem(label="Undo")
    pad.main_grid.menubar.edit_menu.submenu.undo_edit.connect("activate", undo)
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.undo_edit, 0, 1, 0, 1)

    pad.main_grid.menubar.edit_menu.submenu.redo_edit = Gtk.MenuItem(label="Redo")
    pad.main_grid.menubar.edit_menu.submenu.redo_edit.connect("activate", redo)
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.redo_edit, 0, 1, 1, 2)

    pad.main_grid.menubar.edit_menu.submenu.separator_one = Gtk.SeparatorMenuItem()
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.separator_one, 0, 1, 2, 3)

    pad.main_grid.menubar.edit_menu.submenu.cut_edit = Gtk.MenuItem(label="Cut")
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.cut_edit, 0, 1, 3, 4)

    pad.main_grid.menubar.edit_menu.submenu.copy_edit = Gtk.MenuItem(label="Copy")
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.copy_edit, 0, 1, 4, 5)

    pad.main_grid.menubar.edit_menu.submenu.paste_edit = Gtk.MenuItem(label="Paste")
    pad.main_grid.menubar.edit_menu.submenu.paste_edit.connect("activate", paste)
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.paste_edit, 0, 1, 5, 6)

    pad.main_grid.menubar.edit_menu.submenu.delete_edit = Gtk.MenuItem(label="Delete")
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.delete_edit, 0, 1, 6, 7)

    pad.main_grid.menubar.edit_menu.submenu.separator_two = Gtk.SeparatorMenuItem()
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.separator_two, 0, 1, 7, 8)

    pad.main_grid.menubar.edit_menu.submenu.select_all_edit = Gtk.MenuItem(label="Select All")
    pad.main_grid.menubar.edit_menu.submenu.attach(pad.main_grid.menubar.edit_menu.submenu.select_all_edit, 0, 1, 8, 9)

    pad.main_grid.menubar.edit_menu.set_submenu(pad.main_grid.menubar.edit_menu.submenu)
    pad.main_grid.menubar.append(pad.main_grid.menubar.edit_menu)