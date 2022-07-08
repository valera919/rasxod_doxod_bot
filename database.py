import sqlite3


def connect_database():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    return connection, cursor


class InitDB:
    def __init__(self):
        self.connection, self.cursor = connect_database()

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(30) NOT NULL,
            chat_id INTEGER NOT NULL UNIQUE
        )""")

    def create_rasxodi_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS rasxodi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            product_name VARCHAR(30) NOT NULL,
            price INTEGER NOT NULL,
            date VARCHAR(30) NOT NULL
        )""")

    def create_category_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            category_name VARCHAR(20) NOT NULL
        )""")

    def start(self):
        self.create_user_table()
        self.create_rasxodi_table()
        self.create_category_table()


        self.connection.commit()
        self.connection.close()



if __name__ == "__main__":
    InitDB().start()




