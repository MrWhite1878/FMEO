import gameFiles.game as gameInstance

def main():
    game = gameInstance.Game()
    gameType = input("Enter 1 for PvP, 2 for PvAI, 3 for AIvAI: ")

    if gameType == "1":
        game.gameLoopPvP()

    elif gameType == "2":
        userPlayer = input("Enter 1 to play X, 2 for O: ")
        if userPlayer == "1":
            userPlayer = "X"
        elif userPlayer == "2":
            userPlayer = "O"
        else:
            print("Invalid player! Please retry.")
            return
        game.gameLoopPvAI(userPlayer)

    elif gameType == "3":
        game.gameLoopAIvAI()

    else:
        print("Invalid game type! Please retry.")

if __name__ == '__main__':
    while True:
        main()
        if input("Play again? (y/n): ") == "n":
            break