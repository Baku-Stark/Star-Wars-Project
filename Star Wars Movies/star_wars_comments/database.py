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

import sqlite3 as lite

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
cyan = '\033[36m'
end = '\033[m'

def movie_id_convert(id_movie: int):
    """
        Dicionário de conversão de ID.
    """

    movie = {
        1:"The Phantom Menace",
        2:"Attack of the Clones",
        3:"Revenge of the Sith",
        4:"A New Hope",
        5:"The Empire Strikes Back",
        6:"Return of the Jedi"
    }

    return movie[id_movie]

def create_db(id_movie: int):
    """
        Criar o banco de dados com o nome do filme selecionado.
    """

    connection = lite.connect(f'db/{movie_id_convert(id_movie)}.db')

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
        connection.close()

def read_comment(id_movie_rec: int):
    """
        Leitura do banco de dados.

        ...
            
        Return
        ----------
        data : List[]
    """

    # === [1]
    if movie_id_convert(id_movie_rec) == "The Phantom Menace":
        connection = lite.connect(f'db/{movie_id_convert(id_movie_rec)}.db')

    # === [2]
    elif movie_id_convert(id_movie_rec) == "Attack of the Clones":
        connection = lite.connect(f'db/{movie_id_convert(id_movie_rec)}.db')

    # === [3]
    elif movie_id_convert(id_movie_rec) == "Revenge of the Sith":
        connection = lite.connect(f'db/{movie_id_convert(id_movie_rec)}.db')

    # === [4]
    elif movie_id_convert(id_movie_rec) == "A New Hope":
        connection = lite.connect(f'db/{movie_id_convert(id_movie_rec)}.db')

    # === [5]
    elif movie_id_convert(id_movie_rec) == "The Empire Strikes Back":
        connection = lite.connect(f'db/{movie_id_convert(id_movie_rec)}.db')

    # === [6]
    else:
        connection = lite.connect(f'db/{movie_id_convert(id_movie_rec)}.db')

    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM comments")
        data = [data for data in cur.fetchall()]

    connection.close()

    return data

def create_comment(comment, id_movie):
    """
        Leitura do banco de dados.

        ...
            
        ARGs
        ----------
    """

    rec_username = comment['username']
    rec_comment = comment['comment']
    rec_stars_rating = comment['stars_rating']

    lista = [rec_username, rec_comment, rec_stars_rating]

    connection = lite.connect(f'db/{movie_id_convert(id_movie)}.db')

    with connection:
        cur = connection.cursor()
        cur.execute("INSERT INTO comments (username, comment, stars_rating) VALUES (?, ?, ?)", lista)

    connection.close()

    print(green + "[!] NOVO COMENTÁRIO INSERIDO [!]" + end)