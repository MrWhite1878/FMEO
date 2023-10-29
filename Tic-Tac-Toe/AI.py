import Game
import random

class AI:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        # Get a list of all empty cells on the board
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    empty_cells.append([i, j])
        print(empty_cells)
        # Choose a random empty cell
        return random.choice(empty_cells)