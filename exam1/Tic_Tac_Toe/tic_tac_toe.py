import random

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
    if board[int(spot)-1] != '.':
        return True
    else:
        return False


def is_winner(sign):
    if(
        board[0] == sign and board[1] == sign and board[2] == sign or
        board[3] == sign and board[4] == sign and board[5] == sign or
        board[7] == sign and board[7] == sign and board[8] == sign or
        board[0] == sign and board[3] == sign and board[6] == sign or
        board[1] == sign and board[4] == sign and board[7] == sign or
        board[2] == sign and board[5] == sign and board[8] == sign or
        board[2] == sign and board[4] == sign and board[6] == sign or
        board[0] == sign and board[4] == sign and board[8] == sign
    ):
        #print("{} is the winner!".format(sign))
        return True
    else:
        return False


def set_player_move():
    print_board()
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or is_spot_free(int(move)):
        move = input("Enter the position you want(1-9):")
    set_board(int(move)-1, PLAYER_SYMBOL)
    is_winner(PLAYER_SYMBOL)


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
            set_player_move()
            set_computer_move()
    #set_player_move()
    # print(board)
    print_board()

if __name__ == '__main__':
    main()