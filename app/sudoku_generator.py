import random
from app.sudoku_board import SudokuBoard


class SudokuGenerator(SudokuBoard):
    def __init__(self, difficulty='medium'):
        """
        Initializes a new instance of the SudokuGenerator class.
        :param difficulty: The difficulty of the generated Sudoku puzzle.
        """
        # Start with a blank board
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solve()  # This will fill the board with a valid solution
        self.create_puzzle(difficulty)

    def create_puzzle(self, difficulty):
        """
        Creates a Sudoku puzzle with the specified difficulty.
        :param difficulty: The difficulty of the puzzle.
        """
        difficulties = {
            'easy': 20,
            'medium': 30,
            'hard': 40,
        }

        # Ensure difficulty is valid
        if difficulty not in difficulties:
            raise ValueError('Invalid difficulty. ' +
                             f'Choose from {list(difficulties.keys())}.')

        # Remove numbers from filled board to create the puzzle
        for _ in range(difficulties[difficulty]):
            while True:
                row, col = random.randint(0, 8), random.randint(0, 8)
                if self.board[row][col] != 0:
                    self.board[row][col] = 0
                    break
