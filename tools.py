from database import connect_database



class BaseTools:
    def __init__(self):
        self.connection, self.cursor = connect_database()



class UserTools(BaseTools):
    def register_user(self, full_name: str, chat_id: int):
        try:
            self.cursor.execute("""INSERT INTO users(full_name, chat_id)
                VALUES (?, ?)
            """, (full_name, chat_id))
        except:
            pass
        else:
            self.connection.commit()
        finally:
            self.connection.close()

    def get_user_id(self, chat_id: int):
        self.cursor.execute("""SELECT id
            FROM users
            WHERE chat_id =? 
        """, (chat_id, ))
        user_id: int = self.cursor.fetchone()[0]
        self.connection.close()
        return user_id


    def add_rasxod_to_db(self, user_id: int, product_name: str, price: int, date):
        self.cursor.execute("""INSERT INTO rasxodi(user_id, product_name, price, date)
            VALUES (?, ?, ?, ?)
        """, (user_id, product_name, price, date))
        self.connection.commit()
        self.connection.close()

    def add_category_to_db(self, user_id: int, category_name: str):
        self.cursor.execute("""INSERT INTO categories(user_id, category_name)
            VALUES (?, ?)
        """, (user_id, category_name))


class DBTools:
    def __init__(self):
        self.user_tool: UserTools = UserTools()