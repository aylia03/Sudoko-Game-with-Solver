# SudokuGenerator.py
import random
from Board import Board

class SudokuGenerator:
    def __init__(self, board):
        self.board = board

    def fill_diagonal(self):
        for i in range(0, self.board.size, 3):
            self.fill_box(i, i)

    def fill_box(self, row, col):
        nums = random.sample(range(1, 10), 9)
        for i in range(3):
            for j in range(3):
                self.board.grid[row + i][col + j].value = nums.pop()

    def fill_remaining(self, row=0, col=0):
        if col >= self.board.size and row < self.board.size - 1:
            row += 1
            col = 0
        if row >= self.board.size and col >= self.board.size:
            return True
        if row < 3:
            if col < 3:
                col = 3
        elif row < self.board.size - 3:
            if col == (row // 3) * 3:
                col += 3
        else:
            if col == self.board.size - 3:
                row += 1
                col = 0
                if row >= self.board.size:
                    return True
        for num in random.sample(range(1, 10), 9):
            if self.board.is_valid_move(row, col, num):
                self.board.grid[row][col].value = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board.grid[row][col].value = 0
        return False

    def remove_numbers(self, count):
        while count > 0:
            row = random.randint(0, self.board.size - 1)
            col = random.randint(0, self.board.size - 1)
            if self.board.grid[row][col].value != 0:
                self.board.grid[row][col].value = 0
                count -= 1

    def generate_sudoku(self, empty_cells=40):
        self.fill_diagonal()
        self.fill_remaining()
        self.remove_numbers(empty_cells)
        return self.board