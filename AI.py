#https://www.cs.huji.ac.il/w~ai/projects/2013/UlitmateTic-Tac-Toe/files/report.pdf
# 1 is O, 2 is X
import game_logic

class CPU:

    # evaluation values for the minimax algorithm
    evaluation_values = {
        # Since the CPU is O, O is positve and X is negative
        2 : -10000,
        "Tie": 0,
        1: 10000
    }

    def __init__(self):
        pass
    
    def possible_moves(self, board, forceRow, forceCol):
        moves = []
        if forceRow != -1 and forceCol != -1:
            for row in range(3):
                for col in range(3):
                    if board[forceRow][forceCol][row][col] == 0:
                        moves.append((forceRow, forceCol, row, col))
        else:
            for bigRow in range(3):
                for bigCol in range(3):
                    for row in range(3):
                        for col in range(3):
                            if game_logic.smol_check_winner(board, bigRow, bigCol) == None and board[bigRow][bigCol][row][col] == 0:
                                moves.append((bigRow, bigCol, row, col))
        return moves

    # returns the CPU's move
    def getMove(self, board, depth, forceRow, forceCol):
        empty_cells = self.possible_moves(board, forceRow, forceCol)

        best_value = -10000
        best_move = empty_cells[0]

        for move in empty_cells:
            board[move[0]][move[1]][move[2]][move[3]] = 1
            value = self.minimax(board, depth, 2, -10000, 10000, move[2], move[3])
            board[move[0]][move[1]][move[2]][move[3]] = 0
            print("Move: ", move, "Value: ", value)
            if value > best_value:
                best_value = value
                best_move = move

        return best_move

    # minimax algorithm with fail-soft alpha-beta pruning
    def minimax(self, board, depth, player, alpha, beta, forceRow, forceCol):
        '''
        board: the current board state
        depth: the current depth of the tree
        player: the current player
        alpha: the minimum score that the maximizing player is assured of
        beta: the maximum score that the minimizing player is assured of
        forceRow: the row of the last move
        forceCol: the column of the last move
        '''
        if depth == 0:
            return self.heuristic(board)
        
        if game_logic.check_winner(board):
            return self.evaluation_values[game_logic.check_winner(board)]
        
        children = self.possible_moves(board, forceRow, forceCol)
        #print("Children: ", children)

        if player == 1:
            value = -10000
            for child in children:
                board[child[0]][child[1]][child[2]][child[3]] = player
                value = max(value, self.minimax(board, depth - 1, 2, alpha, beta, child[2], child[3]))
                board[child[0]][child[1]][child[2]][child[3]] = 0
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return value
        else:
            value = 10000
            for child in children:
                board[child[0]][child[1]][child[2]][child[3]] = player
                value = min(value, self.minimax(board, depth - 1, 1, alpha, beta, child[2], child[3]))
                board[child[0]][child[1]][child[2]][child[3]] = 0
                beta = min(beta, value)
                if value <= alpha:
                    break
            return value   
        
    def heuristic(self, board):
        evaluation = 0
        for row in range(3):
            for col in range(3):
                if game_logic.smol_check_winner(board, row, col) == 1:
                    evaluation += 100
                elif game_logic.smol_check_winner(board, row, col) == 2:
                    evaluation -= 100
        return evaluation
