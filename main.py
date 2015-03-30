__author__ = 'dragonloverlord'

from gi.repository import Gtk
from gi.repository import GtkSource


class PadWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)

        def undo(menuitem):
            self.main_grid.textarea_container.buffer.undo()

        def redo(menuitem):
            self.main_grid.textarea_container.buffer.redo()

        def save_as(menuitem):
            def close_dialog(button):
                self.main_grid.save_as_dialog.close()

            self.main_grid.save_as_dialog = Gtk.FileChooserDialog()

            self.main_grid.save_as_dialog.close_button = self.main_grid.save_as_dialog.add_button("Close", Gtk.ResponseType.CLOSE)
            self.main_grid.save_as_dialog.close_button.connect("clicked", close_dialog)

            self.main_grid.save_as_dialog.run()

        self.main_grid = Gtk.Grid()
        self.main_grid.set_hexpand(True)
        self.add(self.main_grid)

        self.main_grid.menubar = Gtk.MenuBar()
        self.main_grid.menubar.set_hexpand(True)
        self.main_grid.attach(self.main_grid.menubar, 0, 0, 1, 1)

        self.main_grid.menubar.file_menu = Gtk.MenuItem(label="File")

        self.main_grid.menubar.file_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        self.main_grid.menubar.file_menu.submenu.new_file = Gtk.MenuItem(label="New File")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.new_file, 0, 1, 0, 1)

        self.main_grid.menubar.file_menu.submenu.open_file = Gtk.MenuItem(label="Open...")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.open_file, 0, 1, 1, 2)

        self.main_grid.menubar.file_menu.submenu.save_file = Gtk.MenuItem(label="Save")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.save_file, 0, 1, 2, 3)

        self.main_grid.menubar.file_menu.submenu.save_as = Gtk.MenuItem(label="Save As...")
        self.main_grid.menubar.file_menu.submenu.save_as.connect("activate", save_as)
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.save_as, 0, 1, 3, 4)

        self.main_grid.menubar.file_menu.submenu.separator_menu_item = Gtk.SeparatorMenuItem()
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.separator_menu_item, 0, 1, 4, 5)

        self.main_grid.menubar.file_menu.submenu.quit_pypad = Gtk.MenuItem(label="Quit")
        self.main_grid.menubar.file_menu.submenu.quit_pypad.connect("activate", Gtk.main_quit)
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.quit_pypad, 0, 1, 5, 6)

        self.main_grid.menubar.file_menu.set_submenu(self.main_grid.menubar.file_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.file_menu)

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

        self.main_grid.menubar.options_menu = Gtk.MenuItem(label="Options")

        self.main_grid.menubar.options_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        self.main_grid.menubar.options_menu.submenu.font_options = Gtk.MenuItem(label="Font")
        self.main_grid.menubar.options_menu.submenu.attach(self.main_grid.menubar.options_menu.submenu.font_options, 0, 1, 0, 1)

        self.main_grid.menubar.options_menu.submenu.word_wrap_options = Gtk.MenuItem(label="Word Wrap")
        self.main_grid.menubar.options_menu.submenu.attach(self.main_grid.menubar.options_menu.submenu.word_wrap_options, 0, 1, 1, 2)

        self.main_grid.menubar.options_menu.set_submenu(self.main_grid.menubar.options_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.options_menu)

        self.main_grid.menubar.help_menu = Gtk.MenuItem(label="Help")

        self.main_grid.menubar.help_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        self.main_grid.menubar.help_menu.submenu.about_help = Gtk.MenuItem(label="About")
        self.main_grid.menubar.help_menu.submenu.attach(self.main_grid.menubar.help_menu.submenu.about_help, 0, 1, 0, 1)

        self.main_grid.menubar.help_menu.set_submenu(self.main_grid.menubar.help_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.help_menu)

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
pad.show_all()
Gtk.main()