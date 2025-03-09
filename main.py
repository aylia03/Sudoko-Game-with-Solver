from Board import *
from Solver import Solver
from SudokuGenerator import SudokuGenerator


def main():
    board = Board()

    gen = SudokuGenerator(board)
    gen.generate_sudoku(empty_cells=40)

    print("Generated Sudoku:")
    board.print_board()

    solver = Solver(board)
    if solver.solve():
        print("\nSolved Sudoku:")
        board.print_board()
    else:
        print("\nFailed to solve Sudoku:")

if __name__ == "__main__":
    main()