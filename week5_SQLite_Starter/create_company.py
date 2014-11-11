import sqlite3


def create_database(cursor, db):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT,
                            monthly_salary INTEGER, yearly_bonus INTEGER,
                            possition TEXT)
    ''')
    db.commit()


def insert_into_database(cursor, db):
    cursor.execute('''
        INSERT INTO users(name, monthly_salary, yearly_bonus, possition)
                            VALUES(?,?,?,?)''', ("Ivan Ivanov", 5000, 10000, "Software Developer"))
    db.commit()

    cursor.execute('''
    INSERT INTO users(name, monthly_salary, yearly_bonus, possition)
                        VALUES(?,?,?,?)''', ("Rado Rado", 500, 0, "Technical Support Intern"))
    db.commit()

    cursor.execute('''
    INSERT INTO users(name, monthly_salary, yearly_bonus, possition)
                        VALUES(?,?,?,?)''', ("Ivo Ivo", 1000, 100000, "CEO"))
    db.commit()

    cursor.execute('''
    INSERT INTO users(name, monthly_salary, yearly_bonus, possition)
                        VALUES(?,?,?,?)''', ("Petar Petrov", 3000, 1000, "Marketing Manager"))
    db.commit()

    cursor.execute('''
    INSERT INTO users(name, monthly_salary, yearly_bonus, possition)
                        VALUES(?,?,?,?)''', ("Maria Georgieva", 8000, 10000, "COO"))
    db.commit()


def view_result(cursor):
    result = cursor.execute("SELECT * FROM users")

    for row in result:
        print(row)


def delete_datebase(cursor, db):
    cursor.execute('''DROP TABLE users''')
    db.commit()
    db.close()


def main():
    db = sqlite3.connect('mydb')
    cursor = db.cursor()
    create_database(cursor, db)
    insert_into_database(cursor, db)
    view_result(cursor)
    #delete_datebase(cursor, db)

if __name__ == '__main__':
    main()