__author__ = 'dragonloverlord'

from gi.repository import Gtk
from gi.repository import GtkSource
from pylibs.main_grid import main_grid
from pylibs.menubar import menubar
from pylibs.submenus.file_menu import file_menu


class PadWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)

    def undo(self, menuitem):
        self.main_grid.textarea_container.buffer.undo()

    def redo(self, menuitem):
        self.main_grid.textarea_container.buffer.redo()

    def edit_menu(self):
        self.main_grid.menubar.edit_menu = Gtk.MenuItem(label="Edit")

        self.main_grid.menubar.edit_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        self.main_grid.menubar.edit_menu.submenu.undo_edit = Gtk.MenuItem(label="Undo")
        self.main_grid.menubar.edit_menu.submenu.undo_edit.connect("activate", undo)
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.undo_edit, 0, 1, 0, 1)

        self.main_grid.menubar.edit_menu.submenu.redo_edit = Gtk.MenuItem(label="Redo")
        self.main_grid.menubar.edit_menu.submenu.redo_edit.connect("activate", redo)
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.redo_edit, 0, 1, 1, 2)

        self.main_grid.menubar.edit_menu.submenu.separator_one = Gtk.SeparatorMenuItem()
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.separator_one, 0, 1, 2, 3)

        self.main_grid.menubar.edit_menu.submenu.cut_edit = Gtk.MenuItem(label="Cut")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.cut_edit, 0, 1, 3, 4)

        self.main_grid.menubar.edit_menu.submenu.copy_edit = Gtk.MenuItem(label="Copy")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.copy_edit, 0, 1, 4, 5)

        self.main_grid.menubar.edit_menu.submenu.paste_edit = Gtk.MenuItem(label="Paste")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.paste_edit, 0, 1, 5, 6)

        self.main_grid.menubar.edit_menu.submenu.delete_edit = Gtk.MenuItem(label="Delete")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.delete_edit, 0, 1, 6, 7)

        self.main_grid.menubar.edit_menu.submenu.separator_two = Gtk.SeparatorMenuItem()
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.separator_two, 0, 1, 7, 8)

        self.main_grid.menubar.edit_menu.submenu.select_all_edit = Gtk.MenuItem(label="Select All")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.select_all_edit, 0, 1, 8, 9)

        self.main_grid.menubar.edit_menu.set_submenu(self.main_grid.menubar.edit_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.edit_menu)

    def options_menu(self):
        self.main_grid.menubar.options_menu = Gtk.MenuItem(label="Options")

        self.main_grid.menubar.options_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        self.main_grid.menubar.options_menu.submenu.font_options = Gtk.MenuItem(label="Font")
        self.main_grid.menubar.options_menu.submenu.attach(self.main_grid.menubar.options_menu.submenu.font_options, 0, 1, 0, 1)

        self.main_grid.menubar.options_menu.submenu.word_wrap_options = Gtk.MenuItem(label="Word Wrap")
        self.main_grid.menubar.options_menu.submenu.attach(self.main_grid.menubar.options_menu.submenu.word_wrap_options, 0, 1, 1, 2)

        self.main_grid.menubar.options_menu.set_submenu(self.main_grid.menubar.options_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.options_menu)

    def help_menu(self):
        self.main_grid.menubar.help_menu = Gtk.MenuItem(label="Help")

        self.main_grid.menubar.help_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        self.main_grid.menubar.help_menu.submenu.about_help = Gtk.MenuItem(label="About")
        self.main_grid.menubar.help_menu.submenu.attach(self.main_grid.menubar.help_menu.submenu.about_help, 0, 1, 0, 1)

        self.main_grid.menubar.help_menu.set_submenu(self.main_grid.menubar.help_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.help_menu)

    def textarea_container(self):
        self.main_grid.textarea_container = Gtk.ScrolledWindow(None, None)

        self.main_grid.textarea_container.buffer = GtkSource.Buffer()

        self.main_grid.textarea_container.textarea = Gtk.TextView.new_with_buffer(self.main_grid.textarea_container.buffer)
        self.main_grid.textarea_container.textarea.set_hexpand(True)
        self.main_grid.textarea_container.textarea.set_vexpand(True)
        self.main_grid.textarea_container.textarea.set_wrap_mode(Gtk.WrapMode.WORD)
        self.main_grid.textarea_container.add_with_viewport(self.main_grid.textarea_container.textarea)

        self.main_grid.textarea_container.set_hexpand(True)
        self.main_grid.textarea_container.set_vexpand(True)
        self.main_grid.attach(self.main_grid.textarea_container, 0, 1, 1, 1)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)

main_grid(pad)
menubar(pad)
file_menu(pad)

pad.show_all()
Gtk.main()