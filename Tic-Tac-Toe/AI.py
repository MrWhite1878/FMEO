import Game
import random

class AI:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        # Get a list of all empty cells on the board
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    empty_cells.append([row, col])
        # Choose a random empty cell
        return random.choice(empty_cells)