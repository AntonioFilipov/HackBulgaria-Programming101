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


def make_reservation(cursor, db):
    name = input("Enter your name:")
    number_of_tickets = input("Enter the number of tickets you want to buy:")
    print("You can choose a movie from the list:")
    show_movies(cursor)
    movie_number = input("Enter the number of the movie:")
    show_movie_projections(cursor, movie_number)
    projections = input("Choose a projection:")
    if spots_in_the_hall(cursor, int(projections)) > int(number_of_tickets):
        cursor.execute('''
            INSERT INTO reservations(username, projection_id, row, col)
                                VALUES(?,?,?,?)''', (name, int(projections), 2, 4))
        db.commit()
    else:
        print("There are not enought spots for this projection.")
        show_movie_projections(cursor, movie_number)
    list_of_seats_tuple = ()
    for ticket in range(number_of_tickets):
        temp_seat = input("Choose sit {} <(row, col)>:".format(ticket))
        if temp_seat in list_of_seats_tuple:
            print("This seat is already taken")
            temp_seat = input("Choose sit {} <(row, col)>:".format(ticket))
        else:
            list_of_seats_tuple.append((temp_seat))


def empty_matrix():
    x = [['.' for i in range(10)] for j in range(10)]
    return x

x = [[[] for i in range(11)] for j in range(11)]
def matrix(hall_row, hall_col):
    temp_seat = (hall_row, hall_col)
    list_of_seats_tuple = []
    for i in range(10):
        print ('\n')
        for j in range(10):
            if i == hall_row and j == hall_col:
                if temp_seat in list_of_seats_tuple:
                    print("This seat is already taken")
                else:
                    list_of_seats_tuple.append((temp_seat))
                x[i][j] = 'X'
            else:
                x[i][j] = '.'
            print (x[i][j], end = ' ')

# def matrix(x, hall_row, hall_col):
#     x = [[]]
#     for i, row in enumerate(x):
#         print ('\n')
#         for j, col in enumerate(row):
#             if i == hall_row and j == hall_col:
#                 x[i][j] = 'X'
#             else:
#                 x[i][j] = '.'
#             print (x[i][j], end = ' ')
            

    # for i, row in enumerate(array):
    #     result = ""
    #     for j, seat in enumerate(row):
    #         if hall_row == i and hall_col == j:
    #             result += 'X'
    #         else:
    #             result += str(seat)
    #     print(result)





def main():
    db = sqlite3.connect('cinema')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    print("====================")
    show_movies(cursor)
    print("====================")
    show_movie_projections(cursor, 1)
    print("====================")
    #make_reservation(cursor, db)
    #hall_matrix(1, 2)
    #hall_matrix(0, 0)
    matrix(1, 1)
    matrix(1, 1)
    print("==========")
    #matrix(0, 3)

if __name__ == '__main__':
    main()