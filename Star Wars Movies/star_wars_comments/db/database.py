"""
    Banco de dados integrado com o MYSQL.

    ...

    FUNCTIONS
    ----------
    [CRUD]
        |   create
        |   read
        |   update
        `-> delete
"""

import os
import sqlite3 as lite

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
cyan = '\033[36m'
end = '\033[m'

connection = lite.connect('db/comments.db')

try:
    with connection:
        cur = connection.cursor()
        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS comments(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    comment TEXT,
                    stars_rating INTEGER
                )
            """
        )

except Exception as error:
    print(red + f"[!] ERROR : {error} [!]" + end)

else:
    print(cyan + "[!] BANCO DE DADOS CRIADO COM SUCESSO [!]" + end)

def read_comment():
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM comments")
        data = [dict(data) for data in cur.fetchall()]

    return data