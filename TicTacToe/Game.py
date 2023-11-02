import AI

# Display the game board
def display_board(board):
    print(board[0][0] + "  | " + board[0][1] + " | " + board[0][2])
    print("---+---+---")
    print(board[1][0] + "  | " + board[1][1] + " | " + board[1][2])
    print("---+---+---")
    print(board[2][0] + "  | " + board[2][1] + " | " + board[2][2])

# Handle moves
def handle_move(board, move, player):
    if board[move[0]][move[1]] == " ":
        board[move[0]][move[1]] = player
    else:
        print("ERROR: Invalid move.")

# Game loop
def game_loop():
    # Create the game board
    board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]
    player = "X"
    while True:
        display_board(board)
        if player == "X":
            print("Player " + player + ", it's your turn.")
            playerMove = input("Enter your move in the format 0 0: ")
            playerMove = [int(num) for num in playerMove.split()]
            handle_move(board, playerMove, player)
            player = "O"
        else:
            print("Player " + player + ", it's your turn.")
            cpuMove = AI.get_move(board, player)
            handle_move(board, cpuMove, player)
            player = "X"

        winner = AI.check_win(board)
        if winner:
            display_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(winner + " wins!")
            break

# Start the game
game_loop()