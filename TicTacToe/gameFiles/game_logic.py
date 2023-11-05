def checkWin(board):
        
        # Check Rows
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        # Check Columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return board[0][i]
        # Check Diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        
        # Check for tie
        tie = True
        for row in board:
            for cell in row:
                if cell == " ":
                    tie = False
        if tie:
            return "Tie"
        
        #default
        return False

def isMoveValid(board, row, col):
        if board[row][col] == " ":
            return True
        else:
            return False