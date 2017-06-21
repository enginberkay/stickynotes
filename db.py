import sqlite3


class database:
    def __init__(self):
        self.conn = sqlite3.connect('notebook.db')
        self.cur = self.conn.cursor()
        self.create_table()
        print("database created")

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')

    def insert(self, data):
        self.cur.execute("INSERT INTO notes (content) VALUES (?)", (data))
        self.conn.commit()
        print("inserted data")

    def update(self, id, data):
        self.cur.execute('UPDATE notes SET content = ? WHERE id = ?', (data, id))
        self.conn.commit()
        print("updated row" + id)

    def delete(self, id):
        self.cur.execute('DELETE FROM notes WHERE id = ?', (id))
        self.conn.commit()
        print("deleted row" + id)

    def close_db(self):
        self.cur.close()
        self.conn.close()
