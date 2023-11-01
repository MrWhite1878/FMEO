import AI

# Create the game board
board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]

# Display the game board
def display_board():
    print(board[0][0] + "  | " + board[0][1] + " | " + board[0][2])
    print("---+---+---")
    print(board[1][0] + "  | " + board[1][1] + " | " + board[1][2])
    print("---+---+---")
    print(board[2][0] + "  | " + board[2][1] + " | " + board[2][2])

# Handle moves
def handle_move(move, player):
    if board[move[0]][move[1]] == " ":
        board[move[0]][move[1]] = player
    else:
        print("ERROR: Invalid move.")

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

# Ask the players to take turns placing their markers on the board
player = "X"
while True:
    display_board()
    if player == "X":
        print("Player " + player + ", it's your turn.")
        playerMove = input("Enter your move in the format 0 0: ")
        playerMove = [int(num) for num in playerMove.split()]
        handle_move(playerMove, player)
        player = "O"
    else:
        print("Player " + player + ", it's your turn.")
        cpuMove = AI.get_move(board, player)
        handle_move(cpuMove, player)
        player = "X"

    winner = check_win(board)
    if winner:
        print(winner + " wins!")
        break