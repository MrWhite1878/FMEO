# functional, not amazing, not horrible
# some double checking with its score evaulations should be done
# also more intricate score evaulations should be done
#
# Based on TTT AI, please see that file for more info

# For the Reader ;)
fyi = {0: "Empty", 1: "O", 2: "X"}

def print_board(board):
    for i in range(3):
        for j in range(3):
            print("\t", board[i][j], "\t", end="")
        print()


# Check for a winner in a small board
def smol_check_winner(board, bigRow, bigCol):
    # Check rows
    for row in range(3):
        if (
            board[bigRow][bigCol][row][0]
            == board[bigRow][bigCol][row][1]
            == board[bigRow][bigCol][row][2]
            != 0
        ):
            return board[bigRow][bigCol][row][0]
    # Check columns
    for col in range(3):
        if (
            board[bigRow][bigCol][0][col]
            == board[bigRow][bigCol][1][col]
            == board[bigRow][bigCol][2][col]
            != 0
        ):
            return board[bigRow][bigCol][0][col]
    # Check diagonals
    if (
        board[bigRow][bigCol][0][0]
        == board[bigRow][bigCol][1][1]
        == board[bigRow][bigCol][2][2]
        != 0
    ):
        return board[bigRow][bigCol][0][0]
    if (
        board[bigRow][bigCol][0][2]
        == board[bigRow][bigCol][1][1]
        == board[bigRow][bigCol][2][0]
        != 0
    ):
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
        if (
            smol_check_winner(board, row, 0)
            == smol_check_winner(board, row, 1)
            == smol_check_winner(board, row, 2)
            != None
        ):
            return smol_check_winner(board, row, 0)
    # Check columns
    for col in range(3):
        if (
            smol_check_winner(board, 0, col)
            == smol_check_winner(board, 1, col)
            == smol_check_winner(board, 2, col)
            != None
        ):
            return smol_check_winner(board, 0, col)
    # Check diagonals
    if (
        smol_check_winner(board, 0, 0)
        == smol_check_winner(board, 1, 1)
        == smol_check_winner(board, 2, 2)
        != None
    ):
        return smol_check_winner(board, 0, 0)
    if (
        smol_check_winner(board, 0, 2)
        == smol_check_winner(board, 1, 1)
        == smol_check_winner(board, 2, 0)
        != None
    ):
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
maxEvaluationalValue = 999999
evals = {
    2: maxEvaluationalValue,
    1: -maxEvaluationalValue,
    "Tie": 0,
}


# Returns the score of the board
def evaluate(board):
    if check_winner(board):
        return evals[check_winner(board)]
    score = 0
    # reward/punish for winning/losing board
    for bigRow in range(3):
        for bigCol in range(3):
            if smol_check_winner(board, bigRow, bigCol) == 1:
                score += 100
                # if two in a row 
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if (i!=0 and j!=0) and smol_check_winner(board, bigRow + i, bigCol + j) == 1:
                                score += 100
                        except IndexError:
                            pass
            elif smol_check_winner(board, bigRow, bigCol) == 2:
                score -= 100
                # if two in a row 
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if (i!=0 and j!=0) and (smol_check_winner(board, bigRow + i, bigCol + j) == 2) and (smol_check_winner(board, bigRow - i, bigCol - j) == 1):
                                score += 150
                        except IndexError:
                            pass
    # reward for two in a row on small board
    for bigRow in range(3):
        for bigCol in range(3):
            if smol_check_winner(board, bigRow, bigCol) is None:
                for i in range(3):
                    for j in range(3):
                        if board[bigRow][bigCol][i][j] == 1:
                            for a in range(-1, 2):
                                for b in range(-1, 2):
                                    try:
                                        if (a!=0 and b!=0) and board[bigRow][bigCol][i+a][j+b] == 1:
                                            score += 5
                                    except IndexError:
                                        pass
                        elif board[bigRow][bigCol][i][j] == 2:
                            for a in range(-1, 2):
                                for b in range(-1, 2):
                                    try:
                                        if (a!=0 and b!=0) and (board[bigRow][bigCol][i+a][j+b] == 2) and (board[bigRow][bigCol][i-a][j-b] == 1):
                                            score += 20
                                    except IndexError:
                                        pass
    return -score

    


# You can read more about this alg online (see minimax wiki and TTT AI for a youtube video)
# This is a minimax alg with alpha beta pruning, meaning it creates a data tree of moves,
# assigns each board a value, and then it chooses the best move based on the values
# The alpha beta pruning is a way to make the alg more efficient by not checking moves that
# are obviously bad.
def minimax(board, depth, alpha, beta, player, forcedRow, forcedCol):
    """
    Parameters:
    board: starting node is the board
    depth: how deep into the tree is the node
    alpha: the new current best eval for X
    beta: best eval for O
    player: the maximizing player
    forcedRow: if the player is forced to play in a certain row
    forcedCol: if the player is forced to play in a certain col
    """

    if depth == 0 or (check_winner(board) != False):  # reachs max depth or winning board
        # print("\tEval:", evaluate(board)[0], ", Depth:", depth, ", Board:", print_board(board))
        return evaluate(board)  # returns how deep into the tree it had to go and node value

    if (forcedRow != -1) and (smol_check_winner(board, forcedRow, forcedCol) != None):
        forcedRow, forcedCol = -1, -1

    possible_moves = []
    if forcedRow == -1 and forcedCol == -1:
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if (
                            smol_check_winner(board, bigRow, bigCol) == None
                            and board[bigRow][bigCol][row][col] == 0
                        ):
                            possible_moves.append([bigRow, bigCol, row, col])
    else:
        for row in range(3):
            for col in range(3):
                if board[forcedRow][forcedCol][row][col] == 0:
                    possible_moves.append([forcedRow, forcedCol, row, col])

    # X(2) is the maximizing player
    if player == 2:
        maxEval = -maxEvaluationalValue  # anything < -500 should work
        for child in possible_moves:
            bigRow, bigCol, row, col = child
            board[bigRow][bigCol][row][col] = player
            tempEval = minimax(board, depth - 1, alpha, beta, 1, row, col)
            board[bigRow][bigCol][row][col] = 0
            maxEval = max(maxEval, tempEval)
            #print(f"\tEval: {eval}  Depth: {depth} Move: {[row, col]}")
            if maxEval > beta:  # no need to continue down the tree
                # print("pruned")
                break
            alpha = max(alpha, maxEval)
        return maxEval

    # see above section for explanation
    else:
        minEval = maxEvaluationalValue
        for child in possible_moves:
            bigRow, bigCol, row, col = child
            board[bigRow][bigCol][row][col] = player
            tEval = minimax(board, depth - 1, alpha, beta, 2, row, col)
            board[bigRow][bigCol][row][col] = 0
            minEval = min(minEval, tEval)
            #print(f"\tEval: {eval}  Depth: {depth} Move: {[row, col]}")
            if minEval < alpha:  # no need to continue down the tree
                # print("pruned")
                break
            beta = min(beta, minEval)
        return minEval


# returns the best move
def get_move(board, depth, player, forcedRow, forcedCol):
    bestEval = -maxEvaluationalValue - 1
    bestMove = [-1, -1, -1, -1]
    if forcedRow == -1 and forcedCol == -1:
        for bigRow in range(3):
            for bigCol in range(3):
                for row in range(3):
                    for col in range(3):
                        if (
                            board[bigRow][bigCol][row][col] == 0
                            and smol_check_winner(board, bigRow, bigCol) == None
                        ):
                            board[bigRow][bigCol][row][col] = player
                            moveEval = minimax(board, depth, -maxEvaluationalValue, maxEvaluationalValue, 1, row, col)
                            '''print(
                                "Eval:",
                                moveEval,
                                ", Depth:",
                                depth,
                                ", Move:",
                                [bigRow, bigCol, row, col],
                            )'''
                            board[bigRow][bigCol][row][col] = 0
                            if moveEval > bestEval:
                                bestEval = moveEval
                                bestMove = [bigRow, bigCol, row, col]
    else:
        bigRow = forcedRow
        bigCol = forcedCol
        for row in range(3):
            for col in range(3):
                if board[bigRow][bigCol][row][col] == 0:
                    board[bigRow][bigCol][row][col] = player
                    moveEval = minimax(board, depth, -maxEvaluationalValue, maxEvaluationalValue, 1, row, col)
                    '''print(
                        "Eval:",
                        moveEval,
                        ", Depth:",
                        depth,
                        ", Move:",
                        [bigRow, bigCol, row, col],
                    )'''
                    board[bigRow][bigCol][row][col] = 0
                    if moveEval > bestEval:
                        bestEval = moveEval
                        bestMove = [bigRow, bigCol, row, col]
    print("Move: ", bestMove)
    return bestMove
