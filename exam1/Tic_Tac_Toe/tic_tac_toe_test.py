import unittest
from tic_tac_toe import block_player_to_win
from tic_tac_toe import last_computer_move
PLAYER_SYMBOL = 'X'
COMPUTER_SYMBOL = 'O'


class TestAI(unittest.TestCase):
    def test_block_player_to_win_if_exist(self):
        board = ['X', '.', 'X', '.', '.', '.', '.', '.', '.']
        self.assertEqual(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board), ['X', 'O', 'X', '.', '.', '.', '.', '.', '.'])
        board = ['.', '.', '.', 'X', 'X', '.', '.', '.', '.']
        self.assertEqual(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board), ['.', '.', '.', 'X', 'X', 'O', '.', '.', '.'])
        board = ['.', '.', '.', '.', '.', '.', '.', 'X', 'X']
        self.assertEqual(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board), ['.', '.', '.', '.', '.', '.', 'O', 'X', 'X'])
        board = ['X', '.', '.', '.', 'X', '.', '.', '.', '.']
        self.assertEqual(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board), ['X', '.', '.', '.', 'X', '.', '.', '.', 'O'])
        board = ['.', '.', 'X', '.', '.', '.', 'X', '.', '.']
        self.assertEqual(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board), ['.', '.', 'X', '.', 'O', '.', 'X', '.', '.'])

    def test_block_player_to_win_if_not_exist(self):
        board = ['.', '.', 'X', '.', '.', '.', '.', '.', '.']
        self.assertFalse(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board))
        board = ['.', '.', 'X', '.', '.', '.', '.', 'X', '.']
        self.assertFalse(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board))
        board = ['X', '.', '.', '.', '.', 'X', '.', 'X', '.']
        self.assertFalse(block_player_to_win(PLAYER_SYMBOL, COMPUTER_SYMBOL, board))

    def test_last_computer_move_if_exist(self):
        board = ['O', '.', 'O', '.', '.', '.', '.', '.', '.']
        self.assertEqual(last_computer_move(COMPUTER_SYMBOL, board), ['O', 'O', 'O', '.', '.', '.', '.', '.', '.'])
        board = ['X', '.', 'X', 'O', 'O', '.', '.', '.', '.']
        self.assertEqual(last_computer_move(COMPUTER_SYMBOL, board), ['X', '.', 'X', 'O', 'O', 'O', '.', '.', '.'])
        board = ['X', '.', 'O', '.', '.', '.', '.', 'O', 'O']
        self.assertEqual(last_computer_move(COMPUTER_SYMBOL, board), ['X', '.', 'O', '.', '.', '.', 'O', 'O', 'O'])
        board = ['O', '.', '.', '.', 'O', '.', '.', '.', '.']
        self.assertEqual(last_computer_move(COMPUTER_SYMBOL, board), ['O', '.', '.', '.', 'O', '.', '.', '.', 'O'])
        board = ['.', '.', 'O', '.', '.', '.', 'O', '.', '.']
        self.assertEqual(last_computer_move(COMPUTER_SYMBOL, board), ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'])

    def test_last_computer_move_if_not_exist(self):
        board = ['.', '.', 'O', '.', '.', '.', '.', '.', '.']
        self.assertFalse(last_computer_move(COMPUTER_SYMBOL, board))
        board = ['.', '.', 'O', '.', '.', '.', '.', 'O', '.']
        self.assertFalse(last_computer_move(COMPUTER_SYMBOL, board))
        board = ['O', '.', '.', '.', '.', 'O', '.', 'O', '.']
        self.assertFalse(last_computer_move(COMPUTER_SYMBOL, board))
if __name__ == '__main__':
    unittest.main()
