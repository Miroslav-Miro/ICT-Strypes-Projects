import unittest
from tic_tac_toe import winner, is_there_a_winner, PLAYER_X, PLAYER_O, Board


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Setup a fresh board before each test
        self.empty_board: Board = {
            "1,1": None,
            "1,2": None,
            "1,3": None,
            "2,1": None,
            "2,2": None,
            "2,3": None,
            "3,1": None,
            "3,2": None,
            "3,3": None,
        }

    def test_initial_board_is_empty(self):
        for value in self.empty_board.values():
            self.assertIsNone(value)

    def test_winner_row(self):
        board = self.empty_board.copy()
        board["2,1"] = board["2,2"] = board["2,3"] = PLAYER_X
        self.assertTrue(winner(board))

    def test_winner_column(self):
        board = self.empty_board.copy()
        board["1,1"] = board["2,1"] = board["3,1"] = PLAYER_O
        self.assertTrue(winner(board))

    def test_winner_diagonal(self):
        board = self.empty_board.copy()
        board["1,1"] = board["2,2"] = board["3,3"] = PLAYER_X
        self.assertTrue(winner(board))

    def test_winner_anti_diagonal(self):
        board = self.empty_board.copy()
        board["1,3"] = board["2,2"] = board["3,1"] = PLAYER_O
        self.assertTrue(winner(board))

    def test_no_winner(self):
        board = self.empty_board.copy()
        board["1,1"] = PLAYER_X
        board["1,2"] = PLAYER_O
        board["1,3"] = PLAYER_X
        board["2,1"] = PLAYER_X
        board["2,2"] = PLAYER_O
        board["2,3"] = PLAYER_X
        board["3,1"] = PLAYER_O
        board["3,2"] = PLAYER_X
        board["3,3"] = PLAYER_O
        self.assertFalse(winner(board))

    def test_is_there_a_winner_x(self):
        board = self.empty_board.copy()
        board["1,1"] = board["1,2"] = board["1,3"] = PLAYER_X
        result = is_there_a_winner(board, counter=5)  # Odd => X
        self.assertEqual(result, [False, "----X wins----"])

    def test_is_there_a_winner_o(self):
        board = self.empty_board.copy()
        board["1,1"] = board["2,2"] = board["3,3"] = PLAYER_O
        result = is_there_a_winner(board, counter=4)  # Even => O
        self.assertEqual(result, [False, "----O wins----"])

    def test_is_there_a_winner_still_playing(self):
        board = self.empty_board.copy()
        board["1,1"] = PLAYER_X
        board["1,2"] = PLAYER_O
        result = is_there_a_winner(board, counter=2)
        self.assertEqual(result, [True])


if __name__ == "__main__":
    unittest.main()
