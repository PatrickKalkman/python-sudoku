from app.sudoku_generator import SudokuGenerator


def test_sudoku_solver():
    for difficulty in ['easy', 'medium', 'hard']:
        for _ in range(10):
            sudoku = SudokuGenerator(difficulty)
            assert sudoku.solve(), f"{difficulty} Sudoku puzzle couldn't be solved"
