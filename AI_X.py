# Check for a winner in a small board
def smol_check_winner(board, bigRow, bigCol):
    # Check rows
    for row in range(3):
        if board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][1] == board[bigRow][bigCol][row][2] != 0:
            return board[bigRow][bigCol][row][0]
    # Check columns
    for col in range(3):
        if board[bigRow][bigCol][0][col] == board[bigRow][bigCol][1][col] == board[bigRow][bigCol][2][col] != 0:
            return board[bigRow][bigCol][0][col]
    # Check diagonals
    if board[bigRow][bigCol][0][0] == board[bigRow][bigCol][1][1] == board[bigRow][bigCol][2][2] != 0:
        return board[bigRow][bigCol][0][0]
    if board[bigRow][bigCol][0][2] == board[bigRow][bigCol][1][1] == board[bigRow][bigCol][2][0] != 0:
        return board[bigRow][bigCol][0][2]
    # Check for a tie
    tie = True
    for row in range(3):
        for col in range(3):
            if board[bigRow][bigCol][row][col] == 0:
                tie = False
    if tie:
        return "Tie"
    # No winner yet
    return None

# Check for a winner in the big board
def check_winner(board):
    # Check rows
    for row in range(3):
        if smol_check_winner(board, row, 0) == smol_check_winner(board, row, 1) == smol_check_winner(board, row, 2) != None:
            return smol_check_winner(board, row, 0)
    # Check columns
    for col in range(3):
        if smol_check_winner(board, 0, col) == smol_check_winner(board, 1, col) == smol_check_winner(board, 2, col) != None:
            return smol_check_winner(board, 0, col)
    # Check diagonals
    if smol_check_winner(board, 0, 0) == smol_check_winner(board, 1, 1) == smol_check_winner(board, 2, 2) != None:
        return smol_check_winner(board, 0, 0)
    if smol_check_winner(board, 0, 2) == smol_check_winner(board, 1, 1) == smol_check_winner(board, 2, 0) != None:
        return smol_check_winner(board, 0, 2)
    # Check for a tie
    tie = True
    for row in range(3):
        for col in range(3):
            if smol_check_winner(board, row, col) == None:
                tie = False
    if tie:
        return "Tie"
    # No winner yet
    return None

evals = {
    2: -10,
    1: 10,
    "Tie": 0,
    None: 0
}

def evaluate(board):
    return evals[check_winner(board)]
    
def minimax(board, depth, alpha, beta, player, depthCount, forcedRow, forcedCol):
    '''
    board: starting node is the board
    depth: how deep into the tree is the node
    alpha: the new current best eval for X
    beta: best eval for O
    player: the maximizing player
    depthCount: keeps track of how deep into the tree the node is
    '''
    if depth == 0 or check_winner(board): # reachs max depth or winning board
        return [evaluate(board), depthCount] # returns how deep into the tree it had to go
    
    # O is the maximizing player
    if player == 1:
        depthCount += 1
        maxEval = -1000 # anything < -10 should work
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if board[bigRow][bigCol][row][col] == 0 and forcedRow == bigRow and forcedCol == bigCol:
                            board[bigRow][bigCol][row][col] = player
                            eval = minimax(board, depth - 1, alpha, beta, 2, depthCount, row, col)[0] #all we care about it eval
                            board[bigRow][bigCol][row][col] = 0
                            maxEval = max(maxEval, eval)
                            alpha = max(alpha, eval)
                            if beta <= alpha: # no need to continue down the tree
                                break
        return [maxEval, depthCount]
    # see above section for explanation
    else:
        minEval = 1000
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if board[bigRow][bigCol][row][col] == 0 and forcedRow == bigRow and forcedCol == bigCol:
                            board[bigRow][bigCol][row][col] = player
                            eval = minimax(board, depth - 1, alpha, beta, 1, depthCount, row, col)[0]
                            board[bigRow][bigCol][row][col] = 0
                            minEval = min(minEval, eval)
                            beta = min(beta, eval)
                            if beta <= alpha:
                                break
        return [minEval, depthCount]

# returns the best move 
def get_move(board, player, forcedRow, forcedCol):
    bestEval = 1000
    bestDepth = 100
    bestMove = [-1, -1]
    if forcedRow == -1 and forcedCol == -1:
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if board[bigRow][bigCol][row][col] == 0:
                            board[bigRow][bigCol][row][col] = player
                            moveEval, moveDepth = minimax(board, 1, -1000, 1000, 1, 0, row, col)
                            # print(board, moveEval, moveDepth)
                            board[bigRow][bigCol][row][col] = 0
                            if moveEval < bestEval:
                                bestEval = moveEval
                                bestDepth = moveDepth
                                bestMove = [bigRow, bigCol, row, col]
                            elif moveEval == bestEval and moveDepth < bestDepth: # if its just as good, it chooses the fastest path
                                bestEval = moveEval
                                bestDepth = moveDepth
                                bestMove = [bigRow, bigCol, row, col]
    else:
        bigRow = forcedRow
        bigCol = forcedCol
        for row in range(3):
            for col in range(3):
                if board[bigRow][bigCol][row][col] == 0:
                    board[bigRow][bigCol][row][col] = player
                    moveEval, moveDepth = minimax(board, 1, -1000, 1000, 1, 0, row, col)
                    # print(board, moveEval, moveDepth)
                    board[bigRow][bigCol][row][col] = 0
                    if moveEval < bestEval:
                        bestEval = moveEval
                        bestDepth = moveDepth
                        bestMove = [bigRow, bigCol, row, col]
                    elif moveEval == bestEval and moveDepth < bestDepth: # if its just as good, it chooses the fastest path
                        bestEval = moveEval
                        bestDepth = moveDepth
                        bestMove = [bigRow, bigCol, row, col]
    return bestMove