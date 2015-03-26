__author__ = 'dragonloverlord'

from gi.repository import Gtk


class PadWindow(Gtk.Window):
    def __init__(self):
        #window stuff
        Gtk.Window.__init__(self, title="PyPad")
        self.set_size_request(600, 500)

        #main grid
        self.main_grid = Gtk.Grid()
        self.main_grid.set_hexpand(True)
        self.add(self.main_grid)

        #menubar for main grid
        self.main_grid.menubar = Gtk.MenuBar()
        self.main_grid.menubar.set_hexpand(True)
        self.main_grid.attach(self.main_grid.menubar, 0, 0, 1, 1)

        #file menu item for menubar
        self.main_grid.menubar.file_menu = Gtk.MenuItem(label="File")

        #submenu for file menu
        self.main_grid.menubar.file_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        #new file menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.new_file = Gtk.MenuItem(label="New File")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.new_file, 0, 1, 0, 1)

        #open file menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.open_file = Gtk.MenuItem(label="Open...")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.open_file, 0, 1, 1, 2)

        #save file menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.save_file = Gtk.MenuItem(label="Save")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.save_file, 0, 1, 2, 3)

        #save as menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.save_as = Gtk.MenuItem(label="Save As...")
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.save_as, 0, 1, 3, 4)

        #menu item separator for file submenu
        self.main_grid.menubar.file_menu.submenu.separator_menu_item = Gtk.SeparatorMenuItem()
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.separator_menu_item, 0, 1, 4, 5)

        #quit menu item for file submenu
        self.main_grid.menubar.file_menu.submenu.quit_pypad = Gtk.MenuItem(label="Quit")
        self.main_grid.menubar.file_menu.submenu.quit_pypad.connect("activate", Gtk.main_quit)
        self.main_grid.menubar.file_menu.submenu.attach(self.main_grid.menubar.file_menu.submenu.quit_pypad, 0, 1, 5, 6)

        #attachers and settings
        self.main_grid.menubar.file_menu.set_submenu(self.main_grid.menubar.file_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.file_menu)

        #edit menu item for menubar
        self.main_grid.menubar.edit_menu = Gtk.MenuItem(label="Edit")

        #submenu for edit menu
        self.main_grid.menubar.edit_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        #undo menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.undo_edit = Gtk.MenuItem(label="Undo")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.undo_edit, 0, 1, 0, 1)

        #redo menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.redo_edit = Gtk.MenuItem(label="Redo")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.redo_edit, 0, 1, 1, 2)

        #1st separator for edit submenu
        self.main_grid.menubar.edit_menu.submenu.separator_one = Gtk.SeparatorMenuItem()
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.separator_one, 0, 1, 2, 3)

        #cut menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.cut_edit = Gtk.MenuItem(label="Cut")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.cut_edit, 0, 1, 3, 4)

        #copy menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.copy_edit = Gtk.MenuItem(label="Copy")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.copy_edit, 0, 1, 4, 5)

        #paste menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.paste_edit = Gtk.MenuItem(label="Paste")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.paste_edit, 0, 1, 5, 6)

        #delete menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.delete_edit = Gtk.MenuItem(label="Delete")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.delete_edit, 0, 1, 6, 7)

        #2nd separator for edit submenu
        self.main_grid.menubar.edit_menu.submenu.separator_two = Gtk.SeparatorMenuItem()
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.separator_two, 0, 1, 7, 8)

        #select all menu item for edit submenu
        self.main_grid.menubar.edit_menu.submenu.select_all_edit = Gtk.MenuItem(label="Select All")
        self.main_grid.menubar.edit_menu.submenu.attach(self.main_grid.menubar.edit_menu.submenu.select_all_edit, 0, 1, 8, 9)

        #attachers and settings
        self.main_grid.menubar.edit_menu.set_submenu(self.main_grid.menubar.edit_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.edit_menu)

        #options menu item for menubar
        self.main_grid.menubar.options_menu = Gtk.MenuItem(label="Options")

        #submenu for options menu
        self.main_grid.menubar.options_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        #font menu item for options submenu
        self.main_grid.menubar.options_menu.submenu.font_options = Gtk.MenuItem(label="Font")
        self.main_grid.menubar.options_menu.submenu.attach(self.main_grid.menubar.options_menu.submenu.font_options, 0, 1, 0, 1)

        #word wrap menu item for options submenu
        self.main_grid.menubar.options_menu.submenu.word_wrap_options = Gtk.MenuItem(label="Word Wrap")
        self.main_grid.menubar.options_menu.submenu.attach(self.main_grid.menubar.options_menu.submenu.word_wrap_options, 0, 1, 1, 2)

        #attachers and settings
        self.main_grid.menubar.options_menu.set_submenu(self.main_grid.menubar.options_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.options_menu)

        #help menu item for menubar
        self.main_grid.menubar.help_menu = Gtk.MenuItem(label="Help")

        #submenu for help menu
        self.main_grid.menubar.help_menu.submenu = Gtk.Menu(reserve_toggle_size=True)

        #about menu item for help submenu
        self.main_grid.menubar.help_menu.submenu.about_help = Gtk.MenuItem(label="About")
        self.main_grid.menubar.help_menu.submenu.attach(self.main_grid.menubar.help_menu.submenu.about_help, 0, 1, 0, 1)

        #attachers and settings
        self.main_grid.menubar.help_menu.set_submenu(self.main_grid.menubar.help_menu.submenu)
        self.main_grid.menubar.append(self.main_grid.menubar.help_menu)

        #textarea
        self.main_grid.textarea = Gtk.TextView()
        self.main_grid.textarea.set_hexpand(True)
        self.main_grid.textarea.set_vexpand(True)
        self.main_grid.textarea.set_wrap_mode(Gtk.WrapMode.WORD)
        self.main_grid.attach(self.main_grid.textarea, 0, 1, 1, 1)


pad = PadWindow()
pad.connect("delete-event", Gtk.main_quit)
pad.show_all()
Gtk.main()