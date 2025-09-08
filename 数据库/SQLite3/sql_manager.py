import sqlite3


class SqlManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert(self, data):
        sql = ("INSERT INTO books(title, author, isbn, publisher, publication_year, category, status) VALUES (?,?,?,?,"
               "?,?,?)")
        for item in data:
            self.cursor.execute(sql, item)
        self.conn.commit()


if __name__ == '__main__':
    sql_manager = SqlManager('./db/example.db')
    rows = [
        ['西游记1', '吴承恩1', 'xxxxxxxx', '人民出版社', '2025', '小说', 0],
        ['西游记2', '吴承恩2', 'xxxxxxxx', '人民出版社', '2025', '小说', 0],
        ['西游记3', '吴承恩3', 'xxxxxxxx', '人民出版社', '2025', '小说', 0],
    ]
    sql_manager.insert(rows)
