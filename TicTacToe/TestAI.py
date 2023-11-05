# credit for teaching the basics:
# https://www.youtube.com/watch?v=l-hh51ncgDI


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


# defining eval borders
evals = {"X": -10, 
         "O": 10, 
         "Tie": 0}


# returns if its winning loss or tie
def evaluate(board):
    if check_win(board):
        return evals[check_win(board)]
    

def debuggz(board, moveEval, moveDepth, row, col, count):
    print("\t" * count, end="")
    print(f"Board: {board}")
    print("\t" * count, end="")
    print(f"Eval: {moveEval}, Depth: {moveDepth}, Move: {[row, col]}")

# minimax algorithm
def minimax(board, depth, alpha, beta, player, depthCount):
    """
    board: starting node is the board
    depth: how deep into the tree is the node
    alpha: the new current best eval for X
    beta: best eval for O
    player: the maximizing player
    depthCount: keeps track of how deep into the tree the node is
    """
    if depth == 0 or check_win(board):  # reachs max depth or winning board
        return [evaluate(board), depthCount,]  # returns how deep into the tree it had to go

    # O is the maximizing player
    moves = []
    if player == "O":
        depthCount += 1
        maxEval = -1000  # anything < -10 should work
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    moves.append([row, col])
        for row, col in moves:
            board[row][col] = player
            eval = minimax(board, depth - 1, alpha, beta, "X", depthCount)[0]  # all we care about it eval
            board[row][col] = " "
            maxEval = max(maxEval, eval)
            debuggz(board, eval, depth, row, col, depth)
            alpha = max(alpha, eval)
            if beta <= alpha:  # no need to continue down the tree
                break
        return [maxEval, depthCount]
    # see above section for explanation
    else:
        depthCount += 1
        minEval = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    eval = minimax(board, depth - 1, alpha, beta, "O", depthCount)[0]
                    board[row][col] = " "
                    minEval = min(minEval, eval)
                    debuggz(board, eval, depth, row, col, depth)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return [minEval, depthCount]


# returns the best move
def get_move(board, player, depth):
    bestEval = 1000
    bestDepth = 100
    bestMove = [-1, -1]
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                moveEval, moveDepth = minimax(board, depth, -1000, 1000, "O", 0)
                debuggz(board, moveEval, moveDepth, row, col, 0)
                board[row][col] = " "
                if moveEval < bestEval:
                    bestEval = moveEval
                    bestDepth = moveDepth
                    bestMove = [row, col]
                elif (
                    moveEval == bestEval and moveDepth < bestDepth
                ):  # if its just as good, it chooses the fastest path
                    bestEval = moveEval
                    bestDepth = moveDepth
                    bestMove = [row, col]
    return bestMove
