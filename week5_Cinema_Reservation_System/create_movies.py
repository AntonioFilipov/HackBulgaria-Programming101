import sqlite3


def create_database(cursor, db):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name TEXT,
                            rating REAL)
    ''')
    db.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projections (id INTEGER PRIMARY KEY,movie_id INTEGER, type TEXT,
                            date_projection TEXT, time TEXT,
                            FOREIGN KEY(movie_id) REFERENCES movies(id))
    ''')
    db.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY, username TEXT,
                            projection_id INTEGER, row INTEGER, col INTEGER,
                            FOREIGN KEY(projection_id) REFERENCES projections(id))
    ''')
    db.commit()


def insert_into_database(cursor, db):
    cursor.execute('''
        INSERT INTO movies(name, rating)
                            VALUES(?,?)''', ("The Hunger Games:Catching Fire", 7.9))
    db.commit()

    cursor.execute('''
        INSERT INTO movies(name, rating)
                            VALUES(?,?)''', ("Wreck-It Ralph", 7.8))
    db.commit()

    cursor.execute('''
        INSERT INTO movies(name, rating)
                            VALUES(?,?)''', ("No more Pain", 9))
    db.commit()

    cursor.execute('''
        INSERT INTO projections(movie_id, type, date_projection, time)
                            VALUES(?,?,?,?)''', (1, "3D", "2014-07-20", "14:34:34"))
    db.commit()

    cursor.execute('''
        INSERT INTO projections(movie_id, type, date_projection, time)
                            VALUES(?,?,?,?)''', (1, "2D", "2014/07/20", "14:34:34"))
    db.commit()

    cursor.execute('''
        INSERT INTO projections(movie_id, type, date_projection, time)
                            VALUES(?,?,?,?)''', (1, "4DX", "2014/07/20", "14:34:34"))
    db.commit()

    cursor.execute('''
        INSERT INTO projections(movie_id, type, date_projection, time)
                            VALUES(?,?,?,?)''', (2, "5D", "2014/07/20", "14:34:34"))
    db.commit()


def view_result(cursor):
    result = cursor.execute("SELECT movies.name, projections.type FROM movies INNER JOIN projections ON movies.id = projections.movie_id")

    for row in result:
        print(row)


def delete_database(cursor, db):
    cursor.execute('''DROP TABLE movies''')
    cursor.execute('''DROP TABLE projections''')
    cursor.execute('''DROP TABLE reservations''')
    db.commit()
    #db.close()


def main():
    db = sqlite3.connect('cinema')
    cursor = db.cursor()
    cursor.execute('pragma foreign_keys=ON')
    #delete_datebase(cursor, db)
    create_database(cursor, db)
    insert_into_database(cursor, db)
    #view_result(cursor)
    db.close()

if __name__ == '__main__':
    main()