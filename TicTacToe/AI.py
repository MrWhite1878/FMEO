import random


# Check if the game has been won
def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    # Check for tie
    tie = True
    for row in board:
        for cell in row:
            if cell == " ":
                tie = False
    if tie:
        return "Tie"
    # If no win condition is met, return False
    return False

# defining eval boarders
evals ={
    "X": -10,
    "O": 10, #because we want o to win
    "Tie": 0,
}

# returns if its winning loss or tie
def evaluate(board):
    #print(board)
    #print(check_win(board))
    return evals[check_win(board)]

# minimax algorithm
def minimax(board, depth, player):
    if depth == 0 or check_win(board):
        return evaluate(board)
    
    if player == "X":
        maxEval = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    maxEval = max(maxEval, minimax(board, depth - 1, "O"))
                    board[row][col] = " "
        return maxEval
    else:
        minEval = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    minEval = min(minEval, minimax(board, depth - 1, "X"))
                    board[row][col] = " "
        return minEval

# returns the best move 
def get_move(board, player):
    bestEval = -1000
    bestMove = [-1, -1]
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                moveEval = minimax(board, 1000, "X")
                #print(board, moveEval)
                board[row][col] = " "
                if moveEval > bestEval:
                    bestEval = moveEval
                    bestMove = [row, col]
    return bestMove