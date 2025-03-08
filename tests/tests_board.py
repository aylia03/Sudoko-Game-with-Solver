import unittest
from Board import Board
from Cell import Cell


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_init(self):
        for row in range(9):
            for col in range(9):
                self.assertEqual(self.board.grid[row][col].value, 0)

    def test_valid_move(self):
        self.assertTrue(self.board.is_valid_move(0,0,5))
        self.board.grid[0][0].set_value(5)
        self.assertFalse(self.board.is_valid_move(0,1,5))
        self.assertFalse(self.board.is_valid_move(1,0,5))
        self.assertFalse(self.board.is_valid_move(1,1,5))

    def test_get_empty_cell(self):
        self.board.grid[0][0].set_value(5)
        self.assertEqual(self.board.get_next_empty_cell(),(0,1))
        for row in range(9):
            for col in range(9):
                self.board.grid[row][col].set_value(1)
        self.assertIsNone(self.board.get_next_empty_cell())

    def test_is_solved(self):
        self.assertFalse(self.board.is_solved())

        for row in range(9):
            for col in range(9):
                self.board.grid[row][col].set_value((row * 3 + col) % 9 + 1)

        self.assertTrue(self.board.is_solved())

    def test_print_board(self):
        for row in range(9):
            for col in range(9):
                self.board.grid[row][col].set_value((row * 3 + col) % 9 + 1)
            self.board.print_board()

if __name__ == '__main__':
    unittest.main()
