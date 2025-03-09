# Solver.py
from Board import Board

class Solver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        return self.solve_sudoku()

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()

        if empty_cell is None:
            return self.board.is_solved()

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board.grid[row][col].value = num

                if self.solve_sudoku():
                    return True

                self.board.grid[row][col].value = 0  # Reset cell for backtracking

        return False

    def find_empty_cell(self):
        return self.board.get_next_empty_cell()

    def is_valid(self, row, col, num):
        return self.board.is_valid_move(row, col, num)