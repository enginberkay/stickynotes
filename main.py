import gi, db
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class MainWindow(Gtk.Window):
    def __init__(self, Window_ID, DB_ID, TEXT_PARAM="Write Your Note"):
        Gtk.Window.__init__(self, title="Sticky Notes")
        self.set_border_width(10)
        self.set_default_size(250, 150)
        self.windowID = Window_ID
        self.dbID = DB_ID
        self.TEXT_PARAM = TEXT_PARAM

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
        App.create_blank_window(A)

    def kill(self, widget):
        myDb.delete(self.dbID)
        self.destroy()
        App.delete_window(A, self.windowID)

    def get_changed_text(self, buffer):
        start_iter = buffer.get_start_iter()
        end_iter = buffer.get_end_iter()
        self.text = buffer.get_text(start_iter, end_iter, True)
        print(self.text)
        myDb.update(self.dbID, self.text)

    def set_id(self):
        self.windowID -= 1

    def create_textView(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(self.TEXT_PARAM)
        scrolledwindow.add(self.textview)

class App:
    def __init__(self):
        global myDb
        myDb = db.database()
        self.counter = -1
        self.myWindows = []
        self.initial_window()

    def initial_window(self):
        rows = myDb.select_all()
        if len(rows) == 0:
            self.create_blank_window()
        else:
            self.create_exist_window(rows)

    def create_exist_window(self, rows):
        for id, content in rows:
            self.counter += 1
            window = MainWindow(self.counter, id, content)
            window.connect('delete-event', exit)
            window.show_all()
            self.myWindows.append(window)

    def create_blank_window(self):
        self.counter += 1
        DB_ID = myDb.insert("Write Your Note")
        window = MainWindow(self.counter, DB_ID)
        window.connect('delete-event', exit)
        window.show_all()
        self.myWindows.append(window)

    def delete_window(self, id):
        del self.myWindows[id]
        self.order_by_on(id)
        print(len(self.myWindows))
        if len(self.myWindows) == 0:
            exit(True, True)

    def order_by_on(self, id):
        length = len(self.myWindows) - 1
        while length >= id:
            self.myWindows[length].set_id()
            length -= 1

def exit(self, event):
    print("kapanis")
    myDb.close_db()
    Gtk.main_quit()


A = App()
Gtk.main()
