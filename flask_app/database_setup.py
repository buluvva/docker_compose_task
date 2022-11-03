import sqlite3 as sl
con = sl.connect('products.db',check_same_thread=False)


def create_table():
    with con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS Films')
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Films (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                product TEXT,
                category INTEGER
            );
        """)
        sql = 'INSERT INTO Films (product, category) values(?, ?)'
        data = [
            ('fast and furious', 'racing'),
            ('fast and furious', 'thriller'),
            ('fast and furious', 'action'),
            ('john wick', 'action'),
            ('john wick', 'criminal'),
            ('dead poets society', 'drama'),
            ('dead poets society', 'adventure'),
            ('the grand hotel Budapest', 'criminal'),
            ('the grand hotel Budapest', 'comedy'),
            ('the grand hotel Budapest', 'detective'),
            ('', 'melodrama'),
            ("Intertstellar", ''),
        ]
        cur.executemany(sql, data)
        con.commit()


def execute(query):
    with con:
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data
