import unittest
from tic_tac_game import TicTacGame

class TestValidNum(unittest.TestCase):
    def testType(self):
        game = TicTacGame()
        self.assertEqual(type(game.validate_num("4")), type(4))
    
    def testValue(self):
        game = TicTacGame()
        self.assertEqual(game.validate_num("4"), 4)

class TestCheckWinner(unittest.TestCase):
    def testWin(self):
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
    

    def testNotWin(self):
        game = TicTacGame()
        game.board = ["X", "O", "X", 
                      "O", "X", "O", 
                      "O", "X", "O"
                     ]
        self.assertEqual(game.check_winner(), False)

class TestChangePlayer(unittest.TestCase):
    def testChange(self):
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