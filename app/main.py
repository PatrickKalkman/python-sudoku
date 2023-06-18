from sudoku_generator import SudokuGenerator
from sudoku_gui import SudokuGUI


def main():
    generator = SudokuGenerator('hard')
    gui = SudokuGUI(generator.board)
    gui.show()
    generator.solve()


if __name__ == "__main__":
    main()
