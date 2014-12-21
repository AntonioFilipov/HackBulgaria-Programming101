import sqlite3


def matrix():
    hall = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]
    return hall


def show_movies(cursor):
    result = cursor.execute("SELECT id, name, rating FROM movies ORDER BY rating DESC")
    for row in result:
        print ("[{}] - {} ({})".format(row['id'], row['name'], row['rating']))


def spots_in_the_hall(cursor, projection):
    count = 0
    MAX_SPOTS = 100
    possition = cursor.execute("SELECT row, col FROM reservations WHERE projection_id = ?", (projection, ))
    for row in possition:
        count += 1
        #print("{}-{}".format(row['row'], row['col']))
    return (MAX_SPOTS - count)


def show_movie_projections(cursor, movie):
    movie_name = cursor.execute("SELECT name FROM movies WHERE id = ?", (movie, ))
    for row in movie_name:
        print("Projections for movie '{}':".format(row['name']))

    result = cursor.execute("SELECT id, type, date_projection, time FROM projections WHERE movie_id = ?", (movie, )).fetchall()
    for row in result:
        print ("[{}] - {} {} ({}) Spots:{}".format(row['id'], row['date_projection'], row['time'], row['type'], spots_in_the_hall(cursor, row['id'])))


def print_projection_hall(cursor, projection):
    projection_hall = matrix()
    spot = cursor.execute("SELECT row, col FROM reservations WHERE projection_id = ?", (projection, ))
    for row in spot:
        projection_hall[row['row']][row['col']] = 'X'

    for row in projection_hall:
        print('\n')
        for col in row:
            print (col, end=" ")


def list_of_seats(cursor, projection):
    seats = []
    spot = cursor.execute("SELECT row, col FROM reservations WHERE projection_id = ?", (projection, ))
    for row in spot:
        seats.append((row['row'], row['col']))
    return seats


def make_reservation(cursor, db):
    name = input("Enter your name:")
    number_of_tickets = input("Enter the number of tickets you want to buy:")
    print("You can choose a movie from the list:")
    show_movies(cursor)
    movie_number = input("Enter the number of the movie:")
    show_movie_projections(cursor, movie_number)
    projections = input("Choose a projection:")
    while spots_in_the_hall(cursor, int(projections)) < int(number_of_tickets):
        print("There are not enough spots for this projection.")
        show_movie_projections(cursor, movie_number)
        projections = input("Choose another projection:")
    not_empty_seats = list_of_seats(cursor, projections)
    for ticket in range(int(number_of_tickets)):
        print(print_projection_hall(cursor, projections))
        temp_seat = input("Choose sit {} <(row, col)>:".format(ticket+1))
        while temp_seat in not_empty_seats:
            print("This seat is already taken")
            temp_seat = input("Choose sit {} <(row, col)>:".format(ticket+1))
        not_empty_seats.append((temp_seat))
        row = temp_seat.split(',')[0].strip()
        col = temp_seat.split(',')[1].strip()
        cursor.execute('''
            INSERT INTO reservations(username, projection_id, row, col)
                                VALUES(?,?,?,?)''', (name, int(projections), row, col))
        db.commit()

def main():
    db = sqlite3.connect('cinema')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    print("Welcome to HackBulgaria Cinema")
    command = 3
    while command != 4:
        print("==========================")
        print("Commands are:")
        print("[1] Show movies")
        print("[2] Show movie projections")
        print("[3] Make reservation")
        print("[4] Exit")
        print("==========================")
        command = input("Choose command number:")
        if command == '1':
            show_movies(cursor)
        elif command == '2':
            show_movies(cursor)
            movie = input("Choose a movie number:")
            show_movie_projections(cursor, int(movie))
        elif command == '3':
            make_reservation(cursor, db)
        elif command == '4':
            return

if __name__ == '__main__':
    main()