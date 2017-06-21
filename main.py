import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import db


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(10)
        self.set_default_size(250, 150)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textView()
        self.textbuffer.connect("changed", self.get_changed_text)

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


def App():
    global myDb
    myDb = db.database()
    window = MainWindow()
    window.connect("delete-event", exit)
    window.show_all()


def exit(event, self):
    myDb.close_db()
    Gtk.main_quit()


App()
Gtk.main()
