def evaluate(board):
    # if someone won just report that score
    if check_winner(board):
        return evals[check_winner(board)], []

    # otherwise, score the board (it gets bad)
    else:
        score = 0
        bigVal = 50
        smallVal = 2
        modifier = 0.67
        pavlovs = []
        won_biggies = []

        # Big board score
        for bigRow in range(2):
            for bigCol in range(3):
                # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                if (
                    smol_check_winner(board, bigRow, bigCol)
                    == smol_check_winner(board, bigRow + 1, bigCol)
                    == 1
                ):
                    pavlovs.append("Big Vertical 2 in a row reward")
                    score += bigVal
                elif (
                    smol_check_winner(board, bigRow, bigCol)
                    == smol_check_winner(board, bigRow + 1, bigCol)
                    == 2
                ):
                    pavlovs.append("Big Vertical 2 in a row punishment")
                    score -= bigVal
        for bigRow in range(3):
            for bigCol in range(2):
                if (
                    smol_check_winner(board, bigRow, bigCol)
                    == smol_check_winner(board, bigRow, bigCol + 1)
                    == 1
                ):
                    pavlovs.append("Big Horizontal 2 in a row reward")
                    score += bigVal
                elif (
                    smol_check_winner(board, bigRow, bigCol)
                    == smol_check_winner(board, bigRow, bigCol + 1)
                    == 2
                ):
                    pavlovs.append("Big Horizontal 2 in a row punishment")
                    score -= bigVal
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (
                smol_check_winner(board, bigRow, 0)
                == smol_check_winner(board, bigRow, 1)
                == 2
            ) and (smol_check_winner(board, bigRow, 2) == 1):
                pavlovs.append("Big Horizontal 2 in a row block reward")
                score += bigVal
            elif (
                smol_check_winner(board, bigRow, 0)
                == smol_check_winner(board, bigRow, 1)
                == 1
            ) and (smol_check_winner(board, bigRow, 2) == 2):
                pavlovs.append("Big Horizontal 2 in a row block punishment")
                score -= bigVal
            # Reward for getting two with a space between, punish for letting opponent get two with a space between
            if (
                smol_check_winner(board, bigRow, 0)
                == smol_check_winner(board, bigRow, 2)
                == 1
            ) and (smol_check_winner(board, bigRow, 1) == 0):
                pavlovs.append("Big Horizontal spaced 2 in a row reward")
                score += bigVal
            elif (
                smol_check_winner(board, bigRow, 0)
                == smol_check_winner(board, bigRow, 2)
                == 2
            ) and (smol_check_winner(board, bigRow, 1) == 0):
                pavlovs.append("Big Horizontal spaced 2 in a row punishment")
                score -= bigVal
            for bigCol in range(3):
                # Reward for getting a big board, punish for letting opponent block a big board
                if smol_check_winner(board, bigRow, bigCol) == 1:
                    pavlovs.append("Big board reward")
                    score += bigVal
                    won_biggies.append([bigRow, bigCol])
                elif smol_check_winner(board, bigRow, bigCol) == 2:
                    pavlovs.append("Big board punishment")
                    score -= bigVal
                    won_biggies.append([bigRow, bigCol])
        for bigCol in range(3):
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (
                smol_check_winner(board, 0, bigCol)
                == smol_check_winner(board, 1, bigCol)
                == 2
            ) and (smol_check_winner(board, 2, bigCol) == 1):
                pavlovs.append("Big Vertical 2 in a row block reward")
                score += bigVal
            elif (
                smol_check_winner(board, 0, bigCol)
                == smol_check_winner(board, 1, bigCol)
                == 1
            ) and (smol_check_winner(board, 2, bigCol) == 2):
                pavlovs.append("Big Vertical 2 in a row block punishment")
                score -= bigVal
            # Reward for getting two with a space between, punish for letting opponent get two with a space between
            if (
                smol_check_winner(board, 0, bigCol)
                == smol_check_winner(board, 2, bigCol)
                == 1
            ) and (smol_check_winner(board, 1, bigCol) == 0):
                pavlovs.append("Big Vertical spaced 2 in a row reward")
                score += bigVal
            elif (
                smol_check_winner(board, 0, bigCol)
                == smol_check_winner(board, 2, bigCol)
                == 2
            ) and (smol_check_winner(board, 1, bigCol) == 0):
                pavlovs.append("Big Vertical spaced 2 in a row punishment")
                score -= bigVal
        truth_1, truth_2 = None, None
        if smol_check_winner(board, 0, 0) == smol_check_winner(board, 1, 1):
            truth_1 = smol_check_winner(board, 0, 0)
        elif smol_check_winner(board, 0, 2) == smol_check_winner(board, 1, 1):
            truth_2 = smol_check_winner(board, 0, 2)
        # Reward for getting 2 in a row diagonally, punish for letting opponent get 2 in a row diagonally
        if truth_1 == 1:
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif truth_1 == 2:
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        if truth_2 == 1:
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif truth_2 == 2:
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        if smol_check_winner(board, 2, 0) == smol_check_winner(board, 1, 1) == 1:
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif smol_check_winner(board, 2, 0) == smol_check_winner(board, 1, 1) == 2:
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        if smol_check_winner(board, 2, 2) == smol_check_winner(board, 1, 1) == 1:
            pavlovs.append("Big Diagonal 2 in a row reward")
            score += bigVal
        elif smol_check_winner(board, 2, 2) == smol_check_winner(board, 1, 1) == 2:
            pavlovs.append("Big Diagonal 2 in a row punishment")
            score -= bigVal
        # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
        if (truth_1 == 2) and (smol_check_winner(board, 2, 2) == 1):
            pavlovs.append("Big Diagonal 2 in a row block reward")
            score += bigVal
        elif (truth_1 == 1) and (smol_check_winner(board, 2, 2) == 2):
            pavlovs.append("Big Diagonal 2 in a row block punishment")
            score -= bigVal
        if (truth_2 == 2) and (smol_check_winner(board, 2, 0) == 1):
            pavlovs.append("Big Diagonal 2 in a row block reward")
            score += bigVal
        elif (truth_2 == 1) and (smol_check_winner(board, 2, 0) == 2):
            pavlovs.append("Big Diagonal 2 in a row block punishment")
            score -= bigVal
        # Reward for getting two with a space between, punish for letting opponent get two with a space between
        if (smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 1) and (
            smol_check_winner(board, 1, 1) == 0
        ):
            pavlovs.append("Big Diagonal spaced 2 in a row reward")
            score += bigVal
        elif (
            smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 2
        ) and (smol_check_winner(board, 1, 1) == 0):
            pavlovs.append("Big Diagonal spaced 2 in a row punishment")
            score -= bigVal
        if (smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 1) and (
            smol_check_winner(board, 1, 1) == 0
        ):
            pavlovs.append("Big Diagonal spaced 2 in a row reward")
            score += bigVal
        elif (
            smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 2
        ) and (smol_check_winner(board, 1, 1) == 0):
            pavlovs.append("Big Diagonal spaced 2 in a row punishment")
            score -= bigVal
        # Reward for blocking two with a space between, punish for letting opponent block two with a space between
        if (smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 2) and (
            smol_check_winner(board, 1, 1) == 1
        ):
            pavlovs.append("Big Diagonal spaced 2 in a row block reward")
            score += bigVal
        elif (
            smol_check_winner(board, 0, 0) == smol_check_winner(board, 2, 2) == 1
        ) and (smol_check_winner(board, 1, 1) == 2):
            pavlovs.append("Big Diagonal spaced 2 in a row block punishment")
            score -= bigVal
        if (smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 2) and (
            smol_check_winner(board, 1, 1) == 1
        ):
            pavlovs.append("Big Diagonal spaced 2 in a row block reward")
            score += bigVal
        elif (
            smol_check_winner(board, 0, 2) == smol_check_winner(board, 2, 0) == 1
        ) and (smol_check_winner(board, 1, 1) == 2):
            pavlovs.append("Big Diagonal spaced 2 in a row block punishment")
            score -= bigVal

        # Small board score
        for bigRow in range(3):
            for bigCol in range(3):
                if [bigRow, bigCol] in won_biggies:
                    continue
                for row in range(2):
                    for col in range(3):
                        # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                        if (
                            board[bigRow][bigCol][row][col]
                            == board[bigRow][bigCol][row + 1][col]
                            == 1
                        ):
                            pavlovs.append("Small Vertical 2 in a row reward")
                            score += smallVal
                        elif (
                            board[bigRow][bigCol][row][col]
                            == board[bigRow][bigCol][row + 1][col]
                            == 2
                        ):
                            pavlovs.append("Small Vertical 2 in a row punishment")
                            score -= smallVal
                # Reward for blocking a 2 in a row, punish for letting opponent block a 2 in a row
                for row in range(3):
                    for col in range(2):
                        if (
                            board[bigRow][bigCol][row][col]
                            == board[bigRow][bigCol][row][col + 1]
                            == 1
                        ):
                            pavlovs.append("Small Horizontal 2 in a row reward")
                            score += smallVal
                        elif (
                            board[bigRow][bigCol][row][col]
                            == board[bigRow][bigCol][row][col + 1]
                            == 2
                        ):
                            pavlovs.append("Small Horizontal 2 in a row punishment")
                            score -= smallVal
                    if (
                        board[bigRow][bigCol][row][0]
                        == board[bigRow][bigCol][row][1]
                        == 2
                    ) and (board[bigRow][bigCol][row][2] == 1):
                        pavlovs.append("Small Horizontal 2 in a row block reward")
                        score += modifier * bigVal
                    elif (
                        board[bigRow][bigCol][row][0]
                        == board[bigRow][bigCol][row][1]
                        == 1
                    ) and (board[bigRow][bigCol][row][2] == 2):
                        pavlovs.append("Small Horizontal 2 in a row block punishment")
                        score -= modifier * bigVal
                    # Reward for getting two with a space between, punish for letting opponent get two with a space between
                    if (
                        board[bigRow][bigCol][row][0]
                        == board[bigRow][bigCol][row][2]
                        == 1
                    ) and (board[bigRow][bigCol][row][1] == 0):
                        pavlovs.append("Small Horizontal spaced 2 in a row reward")
                        score += smallVal
                    elif (
                        board[bigRow][bigCol][row][0]
                        == board[bigRow][bigCol][row][2]
                        == 2
                    ) and (board[bigRow][bigCol][row][1] == 0):
                        pavlovs.append("Small Horizontal spaced 2 in a row punishment")
                        score -= smallVal
                for col in range(3):
                    # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
                    if (
                        board[bigRow][bigCol][0][col]
                        == board[bigRow][bigCol][1][col]
                        == 2
                    ) and (board[bigRow][bigCol][2][col] == 1):
                        pavlovs.append("Small Vertical 2 in a row block reward")
                        score += modifier * bigVal
                    elif (
                        board[bigRow][bigCol][0][col]
                        == board[bigRow][bigCol][1][col]
                        == 1
                    ) and (board[bigRow][bigCol][2][col] == 2):
                        pavlovs.append("Small Vertical 2 in a row block punishment")
                        score -= modifier * bigVal
                    # Reward for getting two with a space between, punish for letting opponent get two with a space between
                    if (
                        board[bigRow][bigCol][0][col]
                        == board[bigRow][bigCol][2][col]
                        == 1
                    ) and (board[bigRow][bigCol][1][col] == 0):
                        pavlovs.append("Small Vertical spaced 2 in a row reward")
                        score += smallVal
                    elif (
                        board[bigRow][bigCol][0][col]
                        == board[bigRow][bigCol][2][col]
                        == 2
                    ) and (board[bigRow][bigCol][1][col] == 0):
                        pavlovs.append("Small Vertical spaced 2 in a row punishment")
                        score -= smallVal
                truth_3, truth_4 = None, None
                if board[bigRow][bigCol][0][0] == board[bigRow][bigCol][1][1]:
                    truth_3 = board[bigRow][bigCol][0][0]
                elif board[bigRow][bigCol][0][2] == board[bigRow][bigCol][1][1]:
                    truth_4 = board[bigRow][bigCol][0][2]
                # Reward for getting 2 in a row diagonally, punish for letting opponent get 2 in a row diagonally
                if truth_3 == 1:
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif truth_3 == 2:
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                if truth_4 == 1:
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif truth_4 == 2:
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                if board[bigRow][bigCol][2][0] == board[bigRow][bigCol][1][1] == 1:
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif board[bigRow][bigCol][2][0] == board[bigRow][bigCol][1][1] == 2:
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                if board[bigRow][bigCol][2][2] == board[bigRow][bigCol][1][1] == 1:
                    pavlovs.append("Small Diagonal 2 in a row reward")
                    score += smallVal
                elif board[bigRow][bigCol][2][2] == board[bigRow][bigCol][1][1] == 2:
                    pavlovs.append("Small Diagonal 2 in a row punishment")
                    score -= smallVal
                # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
                if (truth_3 == 2) and (board[bigRow][bigCol][2][2] == 1):
                    pavlovs.append("Small Diagonal 2 in a row block reward")
                    score += modifier * bigVal
                elif (truth_3 == 1) and (board[bigRow][bigCol][2][2] == 2):
                    pavlovs.append("Small Diagonal 2 in a row block punishment")
                    score -= modifier * bigVal
                if (truth_4 == 2) and (board[bigRow][bigCol][2][0] == 1):
                    pavlovs.append("Small Diagonal 2 in a row block reward")
                    score += modifier * bigVal
                elif (truth_4 == 1) and (board[bigRow][bigCol][2][0] == 2):
                    pavlovs.append("Small Diagonal 2 in a row block punishment")
                    score -= modifier * bigVal
                # Reward for getting two with a space between, punish for letting opponent get two with a space between
                if (
                    board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 1
                ) and (board[bigRow][bigCol][1][1] == 0):
                    pavlovs.append("Small Diagonal spaced 2 in a row reward")
                    score += smallVal
                elif (
                    board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 2
                ) and (board[bigRow][bigCol][1][1] == 0):
                    pavlovs.append("Small Diagonal spaced 2 in a row punishment")
                    score -= smallVal
                if (
                    board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 1
                ) and (board[bigRow][bigCol][1][1] == 0):
                    pavlovs.append("Small Diagonal spaced 2 in a row reward")
                    score += smallVal
                elif (
                    board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 2
                ) and (board[bigRow][bigCol][1][1] == 0):
                    score -= smallVal
                # Reward for blocking two with a space between, punish for letting opponent block two with a space between
                if (
                    board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 2
                ) and (board[bigRow][bigCol][1][1] == 1):
                    pavlovs.append("Small Diagonal spaced 2 in a row block reward")
                    score += modifier * bigVal
                elif (
                    board[bigRow][bigCol][0][0] == board[bigRow][bigCol][2][2] == 1
                ) and (board[bigRow][bigCol][1][1] == 2):
                    pavlovs.append("Small Diagonal spaced 2 in a row block punishment")
                    score -= modifier * bigVal
                if (
                    board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 2
                ) and (board[bigRow][bigCol][1][1] == 1):
                    pavlovs.append("Small Diagonal spaced 2 in a row block reward")
                    score += modifier * bigVal
                elif (
                    board[bigRow][bigCol][0][2] == board[bigRow][bigCol][2][0] == 1
                ) and (board[bigRow][bigCol][1][1] == 2):
                    pavlovs.append("Small Diagonal spaced 2 in a row block punishment")
                    score -= modifier * bigVal
        return score, pavlovs