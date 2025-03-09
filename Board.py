from Cell import Cell

class Board:
    def __init__(self):
        self.size = 9
        self.grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]

    def is_valid_move(self,row,col,value):
        for i in range(self.size):
            if self.grid[row][i].value == value or self.grid[i][col].value == value:
                return False

        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.grid[r][c].value == value:
                    return False

        return True

    def get_next_empty_cell(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col].value == 0:
                    return row, col
        return None

    def is_solved(self):
        for row in range(self.size):
            for col in range(self.size):
                value = self.grid[row][col].value
                if value == 0 or self.is_valid_move(row,col,value):
                    return False
        return True

    def print_board(self):
        for row in range(self.size):
            if row % 3 == 0 and row != 0:
                print("-" * (self.size * 2 + 2))  # Dynamic separator length based on board size

            row_values = []
            for col in range(self.size):
                value = self.grid[row][col].value or '.'  # Show . for empty cells

                if col % 3 == 0 and col != 0:
                    row_values.append('|')

                row_values.append(str(value))

            print(" ".join(row_values))

    def reset_grid(self):
        for row in range(self.size):
            for col in range(self.size):
                self.grid[row][col].reset()