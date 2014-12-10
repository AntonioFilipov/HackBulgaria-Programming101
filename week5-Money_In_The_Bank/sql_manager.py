import hashlib
from Client import Client


def create_clients_table(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT
                email TEXT)
                ''')
    conn.commit()


def password_validation(username, password):
    while len(password) < 8:
        print("Weak passowrd! The numeber of symbols must be more than 8!")
        return False

    UPPER_LETTER = 0
    special_symbols = ['!', '?', '@', '#', '.', ',', '/']
    SPECIAL_SYMBOLS = 0
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    DIGIT_CHAR = 0

    for letter in password:
        if letter.isupper():
            UPPER_LETTER = 1
        elif letter in special_symbols:
            SPECIAL_SYMBOLS = 1
        elif letter in digits:
            DIGIT_CHAR = 1
    if username not in password:
        if UPPER_LETTER == 1 and SPECIAL_SYMBOLS == 1 and DIGIT_CHAR == 1:
            return True
    else:
        return False


def hash_password(password):
    hash_object = hashlib.sha1(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def reset_password():
    


def register(conn, cursor, username, password):
        cursor.execute('''
        INSERT INTO clients (username, password)
                             VALUES(?, ?)''', (username, hash_password(password)))
        conn.commit()


def login(conn, cursor, username, password):
    cursor.execute('''SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1''', (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def change_message(conn, cursor, new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    logged_user.set_message(new_message)
    conn.commit()


def change_pass(conn, cursor, new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()
