# functional, not amazing, not horrible
# some double checking with its score evaulations should be done
# also more intricate score evaulations should be done
#
# Based on TTT AI, please see that file for more info

# Check for a winner in a small board
import random


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
    2: -500,
    1: 500,
    "Tie": 0,
}

# Returns the score of the board
def evaluate(board):
    # if someone won just report that score
    if check_winner(board):
        return evals[check_winner(board)], []
    
    # otherwise, score the board (it gets bad)
    else:
        score = 0
        bigVal = 50
        smallVal = 2
        modifier = 0.33
        pavlovs = []
        won_biggies = []

        # Big board score
        for bigRow in range(2):
            for bigCol in range(3):
                # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                if (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow+1, bigCol) == 1):
                    pavlovs.append("Big Vertical 2 in a row reward")
                    score += bigVal
                elif (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow+1, bigCol) == 2):
                    pavlovs.append("Big Vertical 2 in a row punishment")
                    score -= bigVal
        for bigRow in range(3):
            for bigCol in range(2):
                if (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow, bigCol+1) == 1):
                    pavlovs.append("Big Horizontal 2 in a row reward")
                    score += bigVal
                elif (smol_check_winner(board, bigRow, bigCol) == smol_check_winner(board, bigRow, bigCol+1) == 2):
                    pavlovs.append("Big Horizontal 2 in a row punishment")
                    score -= bigVal
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (smol_check_winner(board, bigRow, 0) == smol_check_winner(board, bigRow, 1) == 2) and (smol_check_winner(board, bigRow, 2) == 1):
                pavlovs.append("Big Horizontal 2 in a row block reward")
                score += bigVal
            elif (smol_check_winner(board, bigRow, 0) == smol_check_winner(board, bigRow, 1) == 1) and (smol_check_winner(board, bigRow, 2) == 2):
                pavlovs.append("Big Horizontal 2 in a row block punishment")
                score -= bigVal
            # Reward for getting two with a space between, punish for letting opponent get two with a space between
            if (smol_check_winner(board, bigRow, 0) == smol_check_winner(board, bigRow, 2) == 1) and (smol_check_winner(board, bigRow, 1) == 0):
                pavlovs.append("Big Horizontal spaced 2 in a row reward")
                score += bigVal
            elif (smol_check_winner(board, bigRow, 0) == smol_check_winner(board, bigRow, 2) == 2) and (smol_check_winner(board, bigRow, 1) == 0):
                pavlovs.append("Big Horizontal spaced 2 in a row punishment")
                score -= bigVal
            for bigCol in range(3):
                # Reward for getting a big board, punish for letting opponent block a big board
                if smol_check_winner(board, bigRow, bigCol) == 1:
                    pavlovs.append("Big board reward")
                    score += bigVal
                    won_biggies.append([bigRow, bigCol])
                elif smol_check_winner(board, bigRow, bigCol) == 2:
                    pavlovs.append("Big board punishment")
                    score -= bigVal
                    won_biggies.append([bigRow, bigCol])
        for bigCol in range(3):
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (smol_check_winner(board, 0, bigCol) == smol_check_winner(board, 1, bigCol) == 2) and (smol_check_winner(board, 2, bigCol) == 1):
                pavlovs.append("Big Vertical 2 in a row block reward")
                score += bigVal
            elif (smol_check_winner(board, 0, bigCol) == smol_check_winner(board, 1, bigCol) == 1) and (smol_check_winner(board, 2, bigCol) == 2):
                pavlovs.append("Big Vertical 2 in a row block punishment")
                score -= bigVal
            # Reward for getting two with a space between, punish for letting opponent get two with a space between
            if (smol_check_winner(board, 0, bigCol) == smol_check_winner(board, 2, bigCol) == 1) and (smol_check_winner(board, 1, bigCol) == 0):
                pavlovs.append("Big Vertical spaced 2 in a row reward")
                score += bigVal
            elif (smol_check_winner(board, 0, bigCol) == smol_check_winner(board, 2, bigCol) == 2) and (smol_check_winner(board, 1, bigCol) == 0):
                pavlovs.append("Big Vertical spaced 2 in a row punishment")
                score -= bigVal
        truth_1, truth_2 = None, None
        if smol_check_winner(board, 0, 0) == smol_check_winner(board, 1, 1):
            truth_1 = smol_check_winner(board, 0, 0) 
        elif smol_check_winner(board, 0, 2) == smol_check_winner(board, 1, 1):
            truth_2 = smol_check_winner(board, 0, 2) 
        # Reward for getting 2 in a row diagonally, punish for letting opponent get 2 in a row diagonally
        if truth_1 == 1:
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif truth_1 == 2:
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        if truth_2 == 1:
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif truth_2 == 2:
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        if (smol_check_winner(board, 2, 0) == smol_check_winner(board, 1, 1) == 1):
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif (smol_check_winner(board, 2, 0) == smol_check_winner(board, 1, 1) == 2):
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        if (smol_check_winner(board, 2, 2) == smol_check_winner(board, 1, 1) == 1):
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif (smol_check_winner(board, 2, 2) == smol_check_winner(board, 1, 1) == 2):
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
        if (truth_1 == 2) and (smol_check_winner(board, 2, 2) == 1):
            pavlovs.append("Big Diagonal 2 in a row block reward")
            score += bigVal
        elif (truth_1 == 1) and (smol_check_winner(board, 2, 2) == 2):
            pavlovs.append("Big Diagonal 2 in a row block punishment")
            score -= bigVal
        if (truth_2 == 2) and (smol_check_winner(board, 2, 0) == 1):
            pavlovs.append("Big Diagonal 2 in a row block reward")
            score += bigVal
        elif (truth_2 == 1) and (smol_check_winner(board, 2, 0) == 2):
            pavlovs.append("Big Diagonal 2 in a row block punishment")
            score -= bigVal
        # Reward for getting two with a space between, punish for letting opponent get two with a space between
        if (smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 1) and (smol_check_winner(board, 1, 1) == 0):
            pavlovs.append("Big Diagonal spaced 2 in a row reward")
            score += bigVal
        elif (smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 2) and (smol_check_winner(board, 1, 1) == 0):
            pavlovs.append("Big Diagonal spaced 2 in a row punishment")
            score -= bigVal
        if (smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 1) and (smol_check_winner(board, 1, 1) == 0):
            pavlovs.append("Big Diagonal spaced 2 in a row reward")
            score += bigVal
        elif (smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 2) and (smol_check_winner(board, 1, 1) == 0):
            pavlovs.append("Big Diagonal spaced 2 in a row punishment")
            score -= bigVal
        # Reward for blocking two with a space between, punish for letting opponent block two with a space between
        if (smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 2) and (smol_check_winner(board, 1, 1) == 1):
            pavlovs.append("Big Diagonal spaced 2 in a row block reward")
            score += bigVal
        elif (smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 1) and (smol_check_winner(board, 1, 1) == 2):
            pavlovs.append("Big Diagonal spaced 2 in a row block punishment")
            score -= bigVal
        if (smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 2) and (smol_check_winner(board, 1, 1) == 1):
            pavlovs.append("Big Diagonal spaced 2 in a row block reward")
            score += bigVal
        elif (smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 1) and (smol_check_winner(board, 1, 1) == 2):
            pavlovs.append("Big Diagonal spaced 2 in a row block punishment")
            score -= bigVal
        

        # Small board score
        for bigRow in range(3):
            for bigCol in range(3):
                if [bigRow, bigCol] in won_biggies:
                    continue
                for row in range(2):
                    for col in range(3):
                        # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                        if (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row+1][col] == 1):
                            pavlovs.append("Small Vertical 2 in a row reward")
                            score += smallVal
                        elif (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row+1][col] == 2):
                            pavlovs.append("Small Vertical 2 in a row punishment")
                            score -= smallVal   
                # Reward for blocking a 2 in a row, punish for letting opponent block a 2 in a row
                for row in range(3):
                    for col in range(2):
                        if (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row][col+1] == 1): 
                                pavlovs.append("Small Horizontal 2 in a row reward")
                                score += smallVal
                        elif (board[bigRow][bigCol][row][col] == board[bigRow][bigCol][row][col+1] == 2):
                                pavlovs.append("Small Horizontal 2 in a row punishment")
                                score -= smallVal
                    if (board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][1] == 2) and (board[bigRow][bigCol][row][2] == 1):
                        pavlovs.append("Small Horizontal 2 in a row block reward")
                        score += modifier * bigVal
                    elif (board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][1] == 1) and (board[bigRow][bigCol][row][2] == 2):
                        pavlovs.append("Small Horizontal 2 in a row block punishment")
                        score -= modifier * bigVal
                    # Reward for getting two with a space between, punish for letting opponent get two with a space between
                    if (board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][2] == 1) and (board[bigRow][bigCol][row][1] == 0):
                        pavlovs.append("Small Horizontal spaced 2 in a row reward")
                        score += smallVal
                    elif (board[bigRow][bigCol][row][0] == board[bigRow][bigCol][row][2] == 2) and (board[bigRow][bigCol][row][1] == 0):
                        pavlovs.append("Small Horizontal spaced 2 in a row punishment")
                        score -= smallVal
                for col in range(3):
                    # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
                    if (board[bigRow][bigCol][0][col] == board[bigRow][bigCol][1][col] == 2) and (board[bigRow][bigCol][2][col] == 1):
                        pavlovs.append("Small Vertical 2 in a row block reward")
                        score += modifier * bigVal
                    elif (board[bigRow][bigCol][0][col] == board[bigRow][bigCol][1][col] == 1) and (board[bigRow][bigCol][2][col] == 2):
                        pavlovs.append("Small Vertical 2 in a row block punishment")
                        score -= modifier * bigVal
                    # Reward for getting two with a space between, punish for letting opponent get two with a space between
                    if (board[bigRow][bigCol][0][col] == board[bigRow][bigCol][2][col] == 1) and (board[bigRow][bigCol][1][col] == 0):
                        pavlovs.append("Small Vertical spaced 2 in a row reward")
                        score += smallVal
                    elif (board[bigRow][bigCol][0][col] == board[bigRow][bigCol][2][col] == 2) and (board[bigRow][bigCol][1][col] == 0):
                        pavlovs.append("Small Vertical spaced 2 in a row punishment")
                        score -= smallVal
                truth_3, truth_4 = None, None
                if board[bigRow][bigCol][0][0] == board[bigRow][bigCol][1][1]:
                    truth_3 = board[bigRow][bigCol][0][0]
                elif board[bigRow][bigCol][0][2] == board[bigRow][bigCol][1][1]:
                    truth_4 = board[bigRow][bigCol][0][2]
                # Reward for getting 2 in a row diagonally, punish for letting opponent get 2 in a row diagonally
                if (truth_3 == 1):
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif (truth_3 == 2):
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                if (truth_4 == 1):
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif (truth_4 == 2):
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                if (board[bigRow][bigCol][2][0] == board[bigRow][bigCol][1][1] == 1):
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif (board[bigRow][bigCol][2][0] == board[bigRow][bigCol][1][1] == 2):
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                if (board[bigRow][bigCol][2][2] == board[bigRow][bigCol][1][1] == 1):
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif (board[bigRow][bigCol][2][2] == board[bigRow][bigCol][1][1] == 2):
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
                if (truth_3 == 2) and (board[bigRow][bigCol][2][2] == 1):
                    pavlovs.append("Small Diagonal 2 in a row block reward")
                    score += modifier * bigVal
                elif (truth_3 == 1) and (board[bigRow][bigCol][2][2] == 2):
                    pavlovs.append("Small Diagonal 2 in a row block punishment")
                    score -= modifier * bigVal
                if (truth_4 == 2) and (board[bigRow][bigCol][2][0] == 1):
                    pavlovs.append("Small Diagonal 2 in a row block reward")
                    score += modifier * bigVal
                elif (truth_4 == 1) and (board[bigRow][bigCol][2][0] == 2):
                    pavlovs.append("Small Diagonal 2 in a row block punishment")
                    score -= modifier * bigVal
                # Reward for getting two with a space between, punish for letting opponent get two with a space between
                if (board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 1) and (board[bigRow][bigCol][1][1] == 0):
                    pavlovs.append("Small Diagonal spaced 2 in a row reward")
                    score += smallVal
                elif (board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 2) and (board[bigRow][bigCol][1][1] == 0):
                    pavlovs.append("Small Diagonal spaced 2 in a row punishment")
                    score -= smallVal
                if (board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 1) and (board[bigRow][bigCol][1][1] == 0):
                    pavlovs.append("Small Diagonal spaced 2 in a row reward")
                    score += smallVal
                elif (board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 2) and (board[bigRow][bigCol][1][1] == 0):
                    score -= smallVal
                # Reward for blocking two with a space between, punish for letting opponent block two with a space between
                if (board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 2) and (board[bigRow][bigCol][1][1] == 1):
                    pavlovs.append("Small Diagonal spaced 2 in a row block reward")
                    score += modifier * bigVal
                elif (board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 1) and (board[bigRow][bigCol][1][1] == 2):
                    pavlovs.append("Small Diagonal spaced 2 in a row block punishment")
                    score -= modifier * bigVal
                if (board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 2) and (board[bigRow][bigCol][1][1] == 1):
                    pavlovs.append("Small Diagonal spaced 2 in a row block reward")
                    score += modifier * bigVal
                elif (board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 1) and (board[bigRow][bigCol][1][1] == 2):
                    pavlovs.append("Small Diagonal spaced 2 in a row block punishment")
                    score -= modifier * bigVal
        return score, pavlovs
    
# You can read more about this alg online (see minimax wiki and TTT AI for a youtube video)
# This is a minimax alg with alpha beta pruning, meaning it creates a data tree of moves,
# assigns each board a value, and then it chooses the best move based on the values
# The alpha beta pruning is a way to make the alg more efficient by not checking moves that
# are obviously bad.
def minimax(board, depth, alpha, beta, player, forcedRow, forcedCol):
    '''
    Parameters:
    board: starting node is the board
    depth: how deep into the tree is the node
    alpha: the new current best eval for X
    beta: best eval for O
    player: the maximizing player
    forcedRow: if the player is forced to play in a certain row
    forcedCol: if the player is forced to play in a certain col
    '''

    if depth == 0 or (check_winner(board) != False): # reachs max depth or winning board
        return evaluate(board)[0] # returns how deep into the tree it had to go and node value
    
    possible_moves = []
    # O is the maximizing player
    if player == 1:
        maxEval = -1000 # anything < -500 should work
        if forcedRow == -1 and forcedCol == -1:
            for bigRow in range(3):
                for bigCol in range(3):
                    for row in range(3):
                        for col in range(3):
                            if board[bigRow][bigCol][row][col] == 0 and smol_check_winner(board, bigRow, bigCol) == None:
                                possible_moves.append([bigRow, bigCol, row, col])
            for child in possible_moves:
                bigRow, bigCol, row, col = child
                board[bigRow][bigCol][row][col] = player
                eval = minimax(board, depth - 1, alpha, beta, 2, row, col)
                board[bigRow][bigCol][row][col] = 0
                maxEval = max(maxEval, eval)
                if alpha > beta: # no need to continue down the tree
                    # print("pruned")
                    break
                alpha = max(alpha, eval)
        else:
            for row in range(3):
                for col in range(3):
                    if board[forcedRow][forcedCol][row][col] == 0:
                        possible_moves.append([forcedRow, forcedCol, row, col])
            for child in possible_moves:
                bigRow, bigCol, row, col = child
                board[forcedRow][forcedCol][row][col] = player
                eval = minimax(board, depth - 1, alpha, beta, 2, row, col)
                board[forcedRow][forcedCol][row][col] = 0
                maxEval = max(maxEval, eval)
                if alpha > beta: # no need to continue down the tree
                    # print("pruned")
                    break
                alpha = max(alpha, eval)
        return maxEval
    
    # see above section for explanation
    else:
        minEval = 1000 
        if forcedRow == -1 and forcedCol == -1:
            for bigRow in range(3):
                for bigCol in range(3):
                    for row in range(3):
                        for col in range(3):
                            if board[bigRow][bigCol][row][col] == 0 and smol_check_winner(board, bigRow, bigCol) == None:
                                possible_moves.append([bigRow, bigCol, row, col])
            for child in possible_moves:
                bigRow, bigCol, row, col = child
                board[bigRow][bigCol][row][col] = player
                eval = minimax(board, depth - 1, alpha, beta, 1, row, col)
                board[bigRow][bigCol][row][col] = 0
                maxEval = min(maxEval, eval)
                beta = min(alpha, eval)
                if alpha > beta: # no need to continue down the tree
                    # print("pruned")
                    break
                alpha = max(alpha, eval)
        else:
            for row in range(3):
                for col in range(3):
                     if board[forcedRow][forcedCol][row][col] == 0:
                        possible_moves.append([forcedRow, forcedCol, row, col])
            for child in possible_moves:
                bigRow, bigCol, row, col = child
                board[forcedRow][forcedCol][row][col] = player
                eval = minimax(board, depth - 1, alpha, beta, 1, row, col)
                board[forcedRow][forcedCol][row][col] = 0
                minEval = min(minEval, eval)
                beta = min(alpha, eval)
                if alpha > beta: # no need to continue down the tree
                    # print("pruned")
                    break
                alpha = max(alpha, eval)
        return minEval

# returns the best move 
def get_move(board, depth, player, forcedRow, forcedCol):
    # print("got here")
    bestEval = 1000
    bestMove = [-1, -1, -1, -1]
    if forcedRow == -1 and forcedCol == -1:
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if board[bigRow][bigCol][row][col] == 0 and smol_check_winner(board, bigRow, bigCol) == None:
                            board[bigRow][bigCol][row][col] = player
                            moveEval = minimax(board, depth, -1000, 1000, 1, row, col)
                            print("Eval:", moveEval, ", Depth:", depth, ", Move:", [bigRow, bigCol, row, col])
                            board[bigRow][bigCol][row][col] = 0
                            if moveEval < bestEval:
                                bestEval = moveEval
                                bestMove = [bigRow, bigCol, row, col]
    else:
        bigRow = forcedRow
        bigCol = forcedCol
        for row in range(3):
            for col in range(3):
                if board[bigRow][bigCol][row][col] == 0:
                    board[bigRow][bigCol][row][col] = player
                    moveEval = minimax(board, depth, -1000, 1000, 1, row, col)
                    print("Eval:", moveEval, ", Depth:", depth, ", Move:", [bigRow, bigCol, row, col])
                    board[bigRow][bigCol][row][col] = 0
                    if moveEval < bestEval:
                        bestEval = moveEval
                        bestMove = [bigRow, bigCol, row, col]
    print("Move: ", bestMove)
    return bestMove