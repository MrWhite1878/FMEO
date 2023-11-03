import TTT_AI_O
import TTT_AI_X


# Display the game board
def display_board(board):
    print(board[0][0] + "  | " + board[0][1] + " | " + board[0][2])
    print("---+---+---")
    print(board[1][0] + "  | " + board[1][1] + " | " + board[1][2])
    print("---+---+---")
    print(board[2][0] + "  | " + board[2][1] + " | " + board[2][2])


# Handle moves
def handle_move(board, move, player):
    board[move[0]][move[1]] = player


# Game loop for when user is X
def game_loop_X():
    # Create the game board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"  # X always goes first
    while True:  # ended with a break statement
        display_board(board)
        # X (user)'s turn
        if player == "X":
            print("Player " + player + ", it's your turn.")
            playerMove = input("Enter your move in the format 0 0: ")
            playerMove = [
                int(num) for num in playerMove.split()
            ]  # turns the string input to an array
            # handles invalid moves
            while board[playerMove[0]][playerMove[1]] != " ":
                print("That space is already taken!")
                playerMove = input("Enter your move in the format 0 0: ")
                playerMove = [int(num) for num in playerMove.split()]
            handle_move(board, playerMove, player)
            player = "O"  # AI's turn
        # O (AI)'s turn
        else:
            print("Player " + player + ", it's your turn.")
            cpuMove = TTT_AI_O.get_move(board, player)  # automatically an array
            print("CPU move: " + str(cpuMove))
            handle_move(board, cpuMove, player)
            player = "X"

        winner = TTT_AI_O.check_win(
            board
        )  # check_win is an AI method to avoid circular imports
        if winner:
            display_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(winner + " wins!")
            break


# Game loop for when user is O
# see game_loop_X() for more comments
def game_loop_O():
    # Create the game board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    while True:
        display_board(board)
        if player == "X":
            print("Player " + player + ", it's your turn.")
            cpuMove = TTT_AI_X.get_move(board, player)
            print("CPU move: " + str(cpuMove))
            handle_move(board, cpuMove, player)
            player = "O"
        else:
            print("Player " + player + ", it's your turn.")
            playerMove = input("Enter your move in the format 0 0: ")
            playerMove = [int(num) for num in playerMove.split()]
            while board[playerMove[0]][playerMove[1]] != " ":
                print("That space is already taken!")
                playerMove = input("Enter your move in the format 0 0: ")
                playerMove = [int(num) for num in playerMove.split()]
            handle_move(board, playerMove, player)
            player = "X"

        winner = TTT_AI_O.check_win(board)
        if winner:
            display_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(winner + " wins!")
            break


# Start the game
while True:
    user = input("Do you want to be X or O:")
    if user == "X":
        game_loop_X()
    else:
        game_loop_O()
    again = int(input("Play again? (1 for Yes, -1 for No)"))
    if again < 0:
        break
