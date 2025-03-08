from Board import *

def main():
    board = Board()

    board.grid[0][0].set_value(5)
    board.grid[0][1].set_value(3)
    board.grid[1][0].set_value(6)
    board.grid[4][4].set_value(7)
    board.grid[8][8].set_value(9)

    print("\n--- Initial Board ---")
    board.print_board()

    row, col, value = 2, 2, 4
    print(f"\n--- Setting Value {value} at ({row}, {col}) ---")
    board.grid[row][col].set_value(value)
    board.print_board()


if __name__ == "__main__":
    main()