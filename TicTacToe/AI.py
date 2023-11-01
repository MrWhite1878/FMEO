import random

def get_move(board, player):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append([row, col])
    return random.choice(empty_cells)