import gameFiles.game_logic as game_logic

class CPU:
    # evaluation values for the minimax algorithm
    evaluation_values = {
        "X": 1,
        "Tie": 0,
        "O": -1
    }
    infinity = float("inf")
    negative_infinity = float("-inf")

    def __init__(self, player):
        '''
        player: the player the AI is playing as
        '''
        self.player = player
    
    # generates a list of all possible moves
    def possibleMoves(self, board):
        '''
        board: the current board state
        '''
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    empty_cells.append((row, col))
        return empty_cells

    # returns the best move for the ai
    def getMove(self, board):
        '''
        board: the current board state
        '''
        empty_cells = self.possibleMoves(board)
        if self.player == "X":
            best_value = self.negative_infinity
            best_move = empty_cells[0]
            for move in empty_cells:
                board[move[0]][move[1]] = self.player
                value = self.minimax(board, 9, "O")
                board[move[0]][move[1]] = " "
                if value > best_value:
                    best_value = value
                    best_move = move
        elif self.player == "O":
            best_value = self.infinity
            best_move = empty_cells[0]
            for move in empty_cells:
                board[move[0]][move[1]] = self.player
                value = self.minimax(board, 9, "X")
                board[move[0]][move[1]] = " "
                if value < best_value:
                    best_value = value
                    best_move = move
        return best_move

    # minimax algorithm
    def minimax (self, board, depth, player):
        '''
        board: the current board state
        depth: the current depth of the tree
        player: the current player
        '''
        if depth == 0 or game_logic.checkWin(board):
            return self.evaluation_values[game_logic.checkWin(board)]
        
        children = self.possibleMoves(board)
        
        if player == "X":
            value = self.negative_infinity
            for child in children:
                board[child[0]][child[1]] = player
                value = max(value, self.minimax(board, depth - 1, "O"))
                board[child[0]][child[1]] = " "
            return value
        else:
            value = self.infinity
            for child in children:
                board[child[0]][child[1]] = player
                value = min(value, self.minimax(board, depth - 1, "X"))
                board[child[0]][child[1]] = " "
            return value