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