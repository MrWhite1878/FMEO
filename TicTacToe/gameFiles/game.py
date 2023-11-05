import gameFiles.game_logic as game_logic
import gameFiles.ai as ai


class Game:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.currentPlayer = "X"
        
    def displayBoard(self):
        print(self.board[0][0] + "  | " + self.board[0][1] + " | " + self.board[0][2])
        print("---+---+---")
        print(self.board[1][0] + "  | " + self.board[1][1] + " | " + self.board[1][2])
        print("---+---+---")
        print(self.board[2][0] + "  | " + self.board[2][1] + " | " + self.board[2][2])
        
    def gameLoopPvP(self):

        # Game Loop
        while not game_logic.checkWin(self.board):
            self.displayBoard()
            print("It is " + self.currentPlayer + "'s turn.")
            # Collect Move
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            # Attempt to make move
            if game_logic.isMoveValid(self.board, row, col):
                self.board[row][col] = self.currentPlayer
            else:
                print("Invalid move! Please retry.")
                continue
            # Switch players
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"
            
        # Display win state
        self.displayBoard()
        if game_logic.checkWin(self.board) == "Tie":
            print("It's a tie!")
        else:
            print(game_logic.checkWin(self.board) + " wins!")
    
    def gameLoopPvAI(self, userPlayer):

        # Initialize AI
        if userPlayer == "X":
            aiPlayer = "O"
        elif userPlayer == "O":
            aiPlayer = "X"
        else:
            print("Invalid player! Please retry.")
            return
        AI = ai.CPU(aiPlayer)

        # Game Loop
        while not game_logic.checkWin(self.board):
            self.displayBoard()
            print("It is " + self.currentPlayer + "'s turn.")
            # Collect Moves
            if self.currentPlayer == userPlayer:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
            else:
                row, col = AI.getMove(self.board)
            # Attempt to make move
            if game_logic.isMoveValid(self.board, row, col):
                self.board[row][col] = self.currentPlayer
            else:
                print("Invalid move! Please retry.")
                continue
            # Switch players
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"

        # Display win state
        self.displayBoard()
        if game_logic.checkWin(self.board) == "Tie":
            print("It's a tie!")
        else:
            print(game_logic.checkWin(self.board) + " wins!")
    
    def gameLoopAIvAI(self):

        # Initialize AI
        aiX = ai.CPU("X")
        aiO = ai.CPU("O")

        # Game Loop
        while not game_logic.checkWin(self.board):
            self.displayBoard()
            print("It is " + self.currentPlayer + "'s turn.")
            # Collect Moves
            if self.currentPlayer == "X":
                row, col = aiX.getMove(self.board)
            else:
                row, col = aiO.getMove(self.board)
            # Attempt to make move
            if game_logic.isMoveValid(self.board, row, col):
                self.board[row][col] = self.currentPlayer
            else:
                print("Invalid move! Please retry.")
                continue
            # Switch players
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"

        # Display win state
        self.displayBoard()
        if game_logic.checkWin(self.board) == "Tie":
            print("It's a tie!")
        else:
            print(game_logic.checkWin(self.board) + " wins!")
