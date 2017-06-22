import gi, db
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sticky Notes")
        self.set_border_width(10)
        self.set_default_size(250, 150)

        # Header Bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Sticky Notes"
        self.set_titlebar(header_bar)

        # Delete Note Button
        image = Gtk.Image()
        image.set_from_file('icon_delete.png')
        delete_button = Gtk.Button(label=None, image=image)
        delete_button.connect('clicked', self.kill)
        header_bar.pack_end(delete_button)

        # New Button
        image = Gtk.Image()
        image.set_from_file('icon_new.png')
        new_button = Gtk.Button(label=None, image=image)
        new_button.connect('clicked', self.new)
        header_bar.pack_end(new_button)


        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textView()

        self.textbuffer.connect("changed", self.get_changed_text)

    def new(self, widget):
        App.create_window(self)

    def kill(self, widget):
        self.destroy()

    def get_changed_text(self, buffer):
        start_iter = buffer.get_start_iter()
        end_iter = buffer.get_end_iter()
        self.text = buffer.get_text(start_iter, end_iter, True)
        print(self.text)


    def create_textView(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
                                 + "Select text and click one of the buttons 'bold', 'italic', "
                                 + "or 'underline' to modify the text accordingly.")
        scrolledwindow.add(self.textview)


class App():
    def __init__(self):
        global myDb
        myDb = db.database()
        self.myWindows = []
        self.create_first_window()

    def create_first_window(self):
        window = MainWindow()
        window.connect("delete-event", exit)
        window.show_all()
        self.myWindows.append(window)

    def create_window(self):
        window = MainWindow()
        window.connect('delete-event', exit)
        window.show_all()
        self.myWindows.append(window)


def exit(self, event):
    myDb.close_db()
    Gtk.main_quit()


App()
Gtk.main()
