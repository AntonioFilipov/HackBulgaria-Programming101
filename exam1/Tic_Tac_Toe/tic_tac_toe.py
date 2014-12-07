import random
#знам, че не трябва да правя така
#по-правилно ли е да ги вкарам в main и да ги подавам като аргументи на функциите
#има ли друг начин?
PLAYER_SYMBOL = ''
COMPUTER_SYMBOL = ''
board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']


def print_board():
    counter = 0
    for spot in board:
        counter += 1
        print(spot, end = " ")
        if(counter == 3):
            print('\n')
            counter = 0


def set_board(spot, symbol):
    board[int(spot)] = symbol

# когато една функция не ни интересува какво връща,
# трябва ли да върнем нещо (например празен стринг), или може 
# и без да връщаме нищо
def choose_X_or_O():
    global PLAYER_SYMBOL
    global COMPUTER_SYMBOL
    symbol = ""
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input("Choose X or O:").upper()

    if symbol == 'X':
        PLAYER_SYMBOL = 'X'
        COMPUTER_SYMBOL = 'O'
    else:
        PLAYER_SYMBOL = 'O'
        COMPUTER_SYMBOL = 'X'
    return PLAYER_SYMBOL


def is_spot_free(spot):
    if board[spot] == '.':
        return True
    else:
        return False


def is_winner(sign):
    if(
        board[0] == sign and board[1] == sign and board[2] == sign or
        board[3] == sign and board[4] == sign and board[5] == sign or
        board[6] == sign and board[7] == sign and board[8] == sign or
        board[0] == sign and board[3] == sign and board[6] == sign or
        board[1] == sign and board[4] == sign and board[7] == sign or
        board[2] == sign and board[5] == sign and board[8] == sign or
        board[2] == sign and board[4] == sign and board[6] == sign or
        board[0] == sign and board[4] == sign and board[8] == sign
    ):
        return True
    else:
        return False


def set_player_move():
    print_board()
    move = input("Enter the position (1-9):")
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        move = input("Position out of range(1-9)! Enter new posiition:")

    while not is_spot_free(int(move)-1):
        move = input("The position is already taken! Enter new position:")
    set_board(int(move)-1, PLAYER_SYMBOL)
    is_winner(PLAYER_SYMBOL)
    return int(move)-1


def block_player_to_win():
    block_list = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [2, 4, 6],
                 [0, 4, 8]]

    for line in block_list:
        count = 0
        for i, position in enumerate(line):
            if board[position] == PLAYER_SYMBOL:
                count += 1
            else:
                empty_spot = position
        if count == 2 and board[empty_spot] == '.':
            return set_board(empty_spot, COMPUTER_SYMBOL)
    return False


def last_computer_move():
    win_positions = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [2, 4, 6],
                    [0, 4, 8]]

    for line in win_positions:
        count = 0
        for i, position in enumerate(line):
            if board[position] == COMPUTER_SYMBOL:
                count += 1
            else:
                empty_spot = position
        if count == 2 and board[empty_spot] == '.':
            return set_board(empty_spot, COMPUTER_SYMBOL)
    return False


def game_play():
    player_move = set_player_move()
    if full_board():
        return "Game over"

    if last_computer_move() is False:
        if block_player_to_win() is False:
            set_computer_move()


def set_computer_move():
    free_spots = []
    for i, spot in enumerate(board):
        if spot == '.':
            free_spots.append(i)
    position = random.choice(free_spots)
    set_board(int(position), COMPUTER_SYMBOL)
    is_winner(COMPUTER_SYMBOL)


def full_board():
    if '.' not in board:
        return True
    else:
        return False


def main():

    choose_X_or_O()
    while not full_board():
        if is_winner(PLAYER_SYMBOL):
            print("{} is the winner!".format(PLAYER_SYMBOL))
            break
        elif is_winner(COMPUTER_SYMBOL):
            print("{} is the winner!".format(COMPUTER_SYMBOL))
            break
        else:
            game_play()

    return print_board()

if __name__ == '__main__':
    main()