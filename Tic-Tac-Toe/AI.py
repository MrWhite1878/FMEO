import Game
import random

class AI:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        # Get a list of all empty cells on the board
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
        
        # If there are no empty cells, return None
        if not empty_cells:
            return None
        
        # Select a random empty cell and return its coordinates
        return random.choice(empty_cells)