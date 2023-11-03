# please see TTT_AI_X.py for better comments


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
evals = {
    "X": 10,
    "O": -10,  # because we want o to win
    "Tie": 0,
}


# returns if its winning loss or tie
def evaluate(board):
    return evals[check_win(board)]


# minimax algorithm
def minimax(board, depth, alpha, beta, player, depthCount):
    if depth == 0 or check_win(board):
        return [evaluate(board), depthCount]

    if player == "X":
        depthCount += 1
        maxEval = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    eval = minimax(board, depth - 1, alpha, beta, "O", depthCount)[0]
                    board[row][col] = " "
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return [maxEval, depthCount]
    else:
        depthCount += 1
        minEval = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    eval = minimax(board, depth - 1, alpha, beta, "X", depthCount)[0]
                    board[row][col] = " "
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return [minEval, depthCount]


# returns the best move
def get_move(board, player):
    bestEval = 1000
    bestDepth = 100
    bestMove = [-1, -1]
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                moveEval, moveDepth = minimax(board, 9, -1000, 1000, "X", 0)
                # print(board, moveEval, moveDepth)
                board[row][col] = " "
                if moveEval < bestEval:
                    bestEval = moveEval
                    bestDepth = moveDepth
                    bestMove = [row, col]
                elif moveEval == bestEval and moveDepth < bestDepth:
                    bestEval = moveEval
                    bestDepth = moveDepth
                    bestMove = [row, col]
    return bestMove
