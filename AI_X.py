# functional, not amazing, not horrible
# some double checking with its score evaulations should be done
# also more intricate score evaulations should be done
#
# Based on TTT AI, please see that file for more info

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
    return False

# Works like the board eval in chess
evals = {
    2: -900,
    1: 900,
    "Tie": 0,
}

# Returns the score of the board
def evaluate(board):
    # if someone won just report that score
    if check_winner(board):
        return evals[check_winner(board)]
    # otherwise, score the board (it gets bad)
    else:
        score = 0
        bigVal = 10
        smallVal = 2

        # Big board score
        for bigRow in range(2):
            for bigCol in range(2):
                # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                if (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow+1, bigCol) == 1):
                    score += bigVal
                elif (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow+1, bigCol) == 2):
                    score -= bigVal
                if (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow, bigCol+1) == 1):
                    score += bigVal
                elif (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow, bigCol+1) == 2):
                    score -= bigVal
                if (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow+1, bigCol+1) == 1):
                    score += bigVal
                elif (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow+1, bigCol+1) == 2):
                    score -= bigVal
        for bigRow in range(3):
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (smol_check_winner(board, bigRow, 0) == smol_check_winner(board, bigRow, 1) == 2) and (smol_check_winner(board, bigRow, 2) == 1):
                score += bigVal
            elif (smol_check_winner(board, bigRow, 0) == smol_check_winner(board, bigRow, 1) == 1) and (smol_check_winner(board, bigRow, 2) == 2):
                score -= bigVal
            for bigCol in range(3):
                # Reward for getting a big board, punish for letting opponent block a big board
                if smol_check_winner(board, bigRow, bigCol) == 1:
                    score += bigVal
                elif smol_check_winner(board, bigRow, bigCol) == 2:
                    score -= bigVal
        for bigCol in range(3):
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (smol_check_winner(board, 0, bigCol) == smol_check_winner(board, 1, bigCol) == 2) and (smol_check_winner(board, 2, bigCol) == 1):
                score += bigVal
            elif (smol_check_winner(board, 0, bigCol) == smol_check_winner(board, 1, bigCol) == 1) and (smol_check_winner(board, 2, bigCol) == 2):
                score -= bigVal
        # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
        if (smol_check_winner(board, 0, 0) == smol_check_winner(board, 1, 1) == 2) and (smol_check_winner(board, 2, 2) == 1):
            score += bigVal
        elif (smol_check_winner(board, 0, 0) == smol_check_winner(board, 1, 1) == 1) and (smol_check_winner(board, 2, 2) == 2):
            score -= bigVal
        if (smol_check_winner(board, 0, 2) == smol_check_winner(board, 1, 1) == 2) and (smol_check_winner(board, 2, 0) == 1):
            score += bigVal
        elif (smol_check_winner(board, 0, 2) == smol_check_winner(board, 1, 1) == 1) and (smol_check_winner(board, 2, 0) == 2):
            score -= bigVal

        # Small board score
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(2):
                    for col in range(2):
                        # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                        if (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row+1][col] == 1):
                            score += smallVal
                        elif (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row+1][col] == 2):
                            score -= smallVal
                        if (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row][col+1] == 1): 
                            score += smallVal
                        elif (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row][col+1] == 2):
                            score -= smallVal
                        if (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row+1][col+1] == 1):
                            score += smallVal
                        elif (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row+1][col+1] == 2):
                            score -= smallVal
                # Reward for blocking a 2 in a row, punish for letting opponent block a 2 in a row
                for row in range(3):
                    if (board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][1] == 2) and (board[bigRow][bigCol][row][2] == 1):
                        score += bigVal
                    elif (board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][1] == 1) and (board[bigRow][bigCol][row][2] == 2):
                        score -= bigVal
                for col in range(3):
                    if (board[bigRow][bigCol][0][col] == board[bigRow][bigCol][1][col] == 2) and (board[bigRow][bigCol][2][col] == 1):
                        score += bigVal
                    elif (board[bigRow][bigCol][0][col] == board[bigRow][bigCol][1][col] == 1) and (board[bigRow][bigCol][2][col] == 2):
                        score -= bigVal
                # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
                if (board[bigRow][bigCol][0][0] == board[bigRow][bigCol][1][1] == 2) and (board[bigRow][bigCol][2][2] == 1):
                    score += bigVal
                elif (board[bigRow][bigCol][0][0] == board[bigRow][bigCol][1][1] == 1) and (board[bigRow][bigCol][2][2] == 2):
                    score -= bigVal
                if (board[bigRow][bigCol][0][2] == board[bigRow][bigCol][1][1] == 2) and (board[bigRow][bigCol][2][0] == 1):
                    score += bigVal
                elif (board[bigRow][bigCol][0][2] == board[bigRow][bigCol][1][1] == 1) and (board[bigRow][bigCol][2][0] == 2):
                    score -= bigVal
        return score
    
# You can read more about this alg online (see minimax wiki and TTT AI for a youtube video)
# This is a minimax alg with alpha beta pruning, meaning it creates a data tree of moves,
# assigns each board a value, and then it chooses the best move based on the values
# The alpha beta pruning is a way to make the alg more efficient by not checking moves that
# are obviously bad.
def minimax(board, depth, alpha, beta, player, depthCount, forcedRow, forcedCol):
    '''
    Parameters:
    board: starting node is the board
    depth: how deep into the tree is the node
    alpha: the new current best eval for X
    beta: best eval for O
    player: the maximizing player
    depthCount: keeps track of how deep into the tree the node is
    forcedRow: if the player is forced to play in a certain row
    forcedCol: if the player is forced to play in a certain col
    '''

    if depth == 0 or check_winner(board): # reachs max depth or winning board
        return [evaluate(board), depthCount] # returns how deep into the tree it had to go and node value
    
    # O is the maximizing player
    if player == 1:
        depthCount += 1
        maxEval = -1000 # anything < -500 should work
        if forcedRow == -1 and forcedCol == -1:
            for bigRow in range(3):
                for bigCol in range(3):
                    for row in range(3):
                        for col in range(3):
                            if board[bigRow][bigCol][row][col] == 0 and smol_check_winner(board, bigRow, bigCol) == None:
                                board[bigRow][bigCol][row][col] = player
                                eval = minimax(board, depth - 1, alpha, beta, 2, depthCount, row, col)[0] #all we care about is eval
                                board[bigRow][bigCol][row][col] = 0
                                maxEval = max(maxEval, eval)
                                alpha = max(alpha, eval)
                                if beta <= alpha: # no need to continue down the tree
                                    break
        else:
            for row in range(3):
                for col in range(3):
                    if board[forcedRow][forcedCol][row][col] == 0:
                        board[forcedRow][forcedCol][row][col] = player
                        eval = minimax(board, depth - 1, alpha, beta, 1, depthCount, row, col)[0] #all we care about is eval
                        board[forcedRow][forcedCol][row][col] = 0
                        maxEval = max(maxEval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha: # no need to continue down the tree
                            break
        return [maxEval, depthCount]
    
    # see above section for explanation
    else:
        depthCount += 1
        minEval = 1000 
        if forcedRow == -1 and forcedCol == -1:
            for bigRow in range(3):
                for bigCol in range(3):
                    for row in range(3):
                        for col in range(3):
                            if board[bigRow][bigCol][row][col] == 0 and smol_check_winner(board, bigRow, bigCol) == None:
                                board[bigRow][bigCol][row][col] = player
                                eval = minimax(board, depth - 1, alpha, beta, 1, depthCount, row, col)[0] #all we care about is eval
                                board[bigRow][bigCol][row][col] = 0
                                maxEval = min(maxEval, eval)
                                beta = min(alpha, eval)
                                if beta <= alpha: # no need to continue down the tree
                                    break
        else:
            for row in range(3):
                for col in range(3):
                     if board[forcedRow][forcedCol][row][col] == 0:
                        board[forcedRow][forcedCol][row][col] = player
                        eval = minimax(board, depth - 1, alpha, beta, 1, depthCount, row, col)[0] #all we care about is eval
                        board[forcedRow][forcedCol][row][col] = 0
                        minEval = min(minEval, eval)
                        beta = min(alpha, eval)
                        if beta <= alpha: # no need to continue down the tree
                            break
        return [minEval, depthCount]

# returns the best move 
def get_move(board, depth, player, forcedRow, forcedCol):
    # print("got here")
    bestEval = 1000
    bestDepth = 1000
    bestMove = [-1, -1, -1, -1]
    if forcedRow == -1 and forcedCol == -1:
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if board[bigRow][bigCol][row][col] == 0 and smol_check_winner(board, bigRow, bigCol) == None:
                            board[bigRow][bigCol][row][col] = player
                            # minimax (board, depth, alpha, beta, player, depthCount, forcedRow, forcedCol)
                            # print("got here")
                            moveEval, moveDepth = minimax(board, depth, -1000, 1000, 1, 0, row, col)
                            # print("got here")
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
                    moveEval, moveDepth = minimax(board, depth, -1000, 1000, 1, 0, row, col)
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