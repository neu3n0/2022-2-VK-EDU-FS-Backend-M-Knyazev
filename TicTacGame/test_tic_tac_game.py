"""a"""
import unittest
from tic_tac_game import TicTacGame


class TestValidNum(unittest.TestCase):
    """a"""
    def test_type(self):
        """a"""
        game = TicTacGame()
        self.assertEqual(type(game.validate_num("4")), type(4))

    def test_value(self):
        """a"""
        game = TicTacGame()
        self.assertEqual(game.validate_num("4"), 4)


class TestCheckWinner(unittest.TestCase):
    """a"""
    def test_win(self):
        """a"""
        game = TicTacGame()
        for i in range(3):
            for j in range(3):
                game.board[i * 3 + j] = "X"
            self.assertEqual(game.check_winner(), True)
            game._reset()
        for i in range(3):
            for j in range(3):
                game.board[j * 3 + i] = "O"
            self.assertEqual(game.check_winner(), True)
            game._reset()
        for i in range(0, 9, 4):
            game.board[i] = "X"
        self.assertEqual(game.check_winner(), True)
        game._reset()
        for i in range(2, 7, 2):
            game.board[i] = "O"
        self.assertEqual(game.check_winner(), True)
        game._reset()

    def test_not_win(self):
        """a"""
        game = TicTacGame()
        game.board = ["X", "O", "X",
                      "O", "X", "O",
                      "O", "X", "O"
                     ]
        self.assertEqual(game.check_winner(), False)


class TestChangePlayer(unittest.TestCase):
    """a"""
    def test_change(self):
        """a"""
        game = TicTacGame()
        game.currentPlayer = "X"
        game.playerName1 = "X"
        game.playerName2 = "O"
        game._change_player()
        self.assertEqual(game.currentPlayer, "O")
        game._change_player()
        self.assertEqual(game.currentPlayer, "X")


if __name__ == '__main__':
    unittest.main()
