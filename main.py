import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(10)
        self.set_default_size(250, 150)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textView()
        self.create_button()
        self.textbuffer.connect("changed", self.text_changed)

        GObject.timeout_add_seconds(1, self.timeout)

    def timeout(self):
        print("hello")

    def text_changed(self, iki):
        start_iter = iki.get_start_iter()
        end_iter = iki.get_end_iter()
        self.text = iki.get_text(start_iter, end_iter, True)
        print(self.text)

    def get_text(self):
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        self.text = self.textbuffer.get_text(start_iter, end_iter, True)

    def create_button(self):
        # Button
        self.button = Gtk.Button(label="Yazı al")
        self.button.connect("clicked", self.button_clicked)
        self.grid.attach(self.button, 0, 2, 1, 1)

    def button_clicked(self, widget):
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
        self.get_text()


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
