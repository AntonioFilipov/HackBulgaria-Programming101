import random


def print_board(board):
    counter = 0
    for spot in board:
        counter += 1
        print(spot, end = " ")
        if(counter == 3):
            print('\n')
            counter = 0


def set_board(board, spot, symbol):
    board[int(spot)] = symbol
    return board

# когато една функция не ни интересува какво връща,
# трябва ли да върнем нещо (например празен стринг), или може 
# и без да връщаме нищо. Само заради тестовете ли връщаме нещото?
def choose_X_or_O():
    symbol = ""
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input("Choose X or O:").upper()
    return symbol


def is_spot_free(board, spot):
    if board[spot] == '.':
        return True
    else:
        return False


def is_winner(board, sign):
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


def set_player_move(player_symbol, board):
    print_board(board)
    move = input("Enter the position (1-9):")
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        move = input("Position out of range(1-9)! Enter new posiition:")

    while not is_spot_free(board, int(move)-1):
        move = input("The position is already taken! Enter new position:")
    set_board(board, int(move)-1, player_symbol)
    is_winner(board, player_symbol)
    return int(move)-1


def block_player_to_win(player_symbol, computer_symbol, board):
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
            if board[int(position)] == player_symbol:
                count += 1
            else:
                empty_spot = int(position)
        if count == 2 and board[empty_spot] == '.':
            return set_board(board, empty_spot, computer_symbol)
    return False


def last_computer_move(computer_symbol, board):
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
            if board[int(position)] == computer_symbol:
                count += 1
            else:
                empty_spot = int(position)
        if count == 2 and board[empty_spot] == '.':
            return set_board(board, empty_spot, computer_symbol)
    return False


def game_play(player_symbol, computer_symbol, board):
    player_move = set_player_move(player_symbol, board)
    if full_board(board):
        return "Game over"

    if last_computer_move(computer_symbol, board) is False:
        if block_player_to_win(player_symbol, computer_symbol, board) is False:
            set_computer_move(computer_symbol, board)


def set_computer_move(computer_symbol, board):
    free_spots = []
    for i, spot in enumerate(board):
        if spot == '.':
            free_spots.append(i)
    position = random.choice(free_spots)
    set_board(board, int(position), computer_symbol)
    is_winner(board, computer_symbol)


def full_board(board):
    if '.' not in board:
        return True
    else:
        return False


def main():
    board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    symbol = choose_X_or_O()
    if symbol == 'X':
        player_symbol = 'X'
        computer_symbol = 'O'
    else:
        player_symbol = 'O'
        computer_symbol = 'X'

    while not full_board(board):
        if is_winner(board, player_symbol):
            print("{} is the winner!".format(player_symbol))
            break
        elif is_winner(board, computer_symbol):
            print("{} is the winner!".format(computer_symbol))
            break
        else:
            game_play(player_symbol, computer_symbol, board)
    return print_board(board)

if __name__ == '__main__':
    main()