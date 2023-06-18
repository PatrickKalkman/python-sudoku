import tkinter as tk

class SudokuGUI:
    def __init__(self, board):
        self.board = board
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")

    def draw_board(self):
        frames = [[tk.Frame(self.window, borderwidth=2, relief="solid") for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                frame = frames[i//3][j//3]
                frame.grid(row=i//3, column=j//3)

                text = "" if self.board[i][j] == 0 else str(self.board[i][j])
                cell = tk.Label(frame, text=text, font=("Arial", 20), width=2, relief="solid", bd=1)
                cell.grid(row=i%3, column=j%3)

    def show(self):
        self.draw_board()
        self.window.mainloop()
