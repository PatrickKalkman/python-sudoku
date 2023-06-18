class SudokuBoard:
    def __init__(self, board):
        """
        Initializes a new instance of the SudokuBoard class.
        :param board: A 2D list representing a Sudoku board.
        """
        self.board = board

    def is_valid(self, row, col, num):
        """
        Checks whether it's valid to place a number in a given position.
        :param row: The row to check.
        :param col: The column to check.
        :param num: The number to check.
        :return: True if placement is valid, False otherwise.
        """
        return all([
            self.is_row_valid(row, num),
            self.is_col_valid(col, num),
            self.is_box_valid(row, col, num)
        ])

    def is_row_valid(self, row, num):
        """Checks if the number already exists in the row."""
        return num not in self.board[row]

    def is_col_valid(self, col, num):
        """Checks if the number already exists in the column."""
        return num not in [self.board[i][col] for i in range(9)]

    def is_box_valid(self, row, col, num):
        """Checks if the number already exists in the box."""
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def find_empty(self):
        """
        Finds an empty space on the board.
        :return: (row, col) pair. If no spaces are left, return (-1, -1).
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i, j
        return -1, -1

    def solve(self):
        """
        Solves the Sudoku board using backtracking.
        :return: True if a solution exists, False otherwise.
        """
        row, col = self.find_empty()

        if row == -1:  # No more empty spaces, we've solved it!
            return True

        for num in range(1, 10):  # Try numbers 1-9
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():  # Recursively try to fill in the rest
                    return True
                self.board[row][col] = 0  # Undo if this branch didn't lead to a solution

        return False  # If no number can be placed, start backtracking

    def print_board(self):
        """
        Prints the Sudoku board.
        """
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:  # Last element
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
