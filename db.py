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
        self.cur.execute("INSERT INTO notes (content) VALUES (?)", (data,))
        self.conn.commit()
        self.cur.execute('SELECT id FROM notes ORDER BY id DESC LIMIT 1')
        id = self.cur.fetchone()
        print("inserted data")
        return id

    def update(self, id, data):
        try:
            self.cur.execute('UPDATE notes SET content = (?) WHERE id = (?)', (data, id[0]))
            self.conn.commit()
        except Exception as ex:
            print(ex)
        else:
            print("updated row", id)

    def delete(self, id):
        self.cur.execute('DELETE FROM notes WHERE id = ?', (id))
        self.conn.commit()
        print("deleted row", id)

    def select_all(self):
        self.cur.execute('SELECT * FROM notes')
        data = self.cur.fetchall()
        return data

    def close_db(self):
        self.cur.close()
        self.conn.close()
