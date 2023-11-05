else:
        score = 0
        value = 1
        pavlovs = []
        for row in range(2):
            for col in range(3):
                # Reward for having getting 2 in a row, punish for letting opponent get 2 in a row
                if (
                    board[row][col]
                    == board[row + 1][col]
                    == 1
                ):
                    pavlovs.append("Small Vertical 2 in a row reward")
                    score += value
                elif (
                    board[row][col]
                    == board[row + 1][col]
                    == 2
                ):
                    pavlovs.append("Small Vertical 2 in a row punishment")
                    score -= value
        # Reward for blocking a 2 in a row, punish for letting opponent block a 2 in a row
        for row in range(3):
            for col in range(2):
                if (
                    board[row][col]
                    == board[row][col + 1]
                    == 1
                ):
                    pavlovs.append("Small Horizontal 2 in a row reward")
                    score += value
                elif (
                    board[row][col]
                    == board[row][col + 1]
                    == 2
                ):
                    pavlovs.append("Small Horizontal 2 in a row punishment")
                    score -= value
            if (
                board[row][0]
                == board[row][1]
                == 2
            ) and (board[row][2] == 1):
                pavlovs.append("Small Horizontal 2 in a row block reward")
                score += value
            elif (
                board[row][0]
                == board[row][1]
                == 1
            ) and (board[row][2] == 2):
                pavlovs.append("Small Horizontal 2 in a row block punishment")
                score -= value
            # Reward for getting two with a space between, punish for letting opponent get two with a space between
            if (
                board[row][0]
                == board[row][2]
                == 1
            ) and (board[row][1] == 0):
                pavlovs.append("Small Horizontal spaced 2 in a row reward")
                score += value
            elif (
                board[row][0]
                == board[row][2]
                == 2
            ) and (board[row][1] == 0):
                pavlovs.append("Small Horizontal spaced 2 in a row punishment")
                score -= value
        for col in range(3):
            # Reward for blocking 2 in a row, punish for letting opponent block 2 in a row
            if (
                board[0][col]
                == board[1][col]
                == 2
            ) and (board[2][col] == 1):
                pavlovs.append("Small Vertical 2 in a row block reward")
                score += value
            elif (
                board[0][col]
                == board[1][col]
                == 1
            ) and (board[2][col] == 2):
                pavlovs.append("Small Vertical 2 in a row block punishment")
                score -= value
            # Reward for getting two with a space between, punish for letting opponent get two with a space between
            if (
                board[0][col]
                == board[2][col]
                == 1
            ) and (board[1][col] == 0):
                pavlovs.append("Small Vertical spaced 2 in a row reward")
                score += value
            elif (
                board[0][col]
                == board[2][col]
                == 2
            ) and (board[1][col] == 0):
                pavlovs.append("Small Vertical spaced 2 in a row punishment")
                score -= value
        truth_3, truth_4 = None, None
        if board[0][0] == board[1][1]:
            truth_3 = board[0][0]
        elif board[0][2] == board[1][1]:
            truth_4 = board[0][2]
        # Reward for getting 2 in a row diagonally, punish for letting opponent get 2 in a row diagonally
        if truth_3 == 1:
            pavlovs.append("Small Diagonal 2 in a row reward")
            score += value
        elif truth_3 == 2:
            pavlovs.append("Small Diagonal 2 in a row punishment")
            score -= value
        if truth_4 == 1:
            pavlovs.append("Small Diagonal 2 in a row reward")
            score += value
        elif truth_4 == 2:
            pavlovs.append("Small Diagonal 2 in a row punishment")
            score -= value
        if board[2][0] == board[1][1] == 1:
            pavlovs.append("Small Diagonal 2 in a row reward")
            score += value
        elif board[2][0] == board[1][1] == 2:
            pavlovs.append("Small Diagonal 2 in a row punishment")
            score -= value
        if board[2][2] == board[1][1] == 1:
            pavlovs.append("Small Diagonal 2 in a row reward")
            score += value
        elif board[2][2] == board[1][1] == 2:
            pavlovs.append("Small Diagonal 2 in a row punishment")
            score -= value
        # Reward for blocking 2 in a row diagonally, punish for letting opponent block 2 in a row diagonally
        if (truth_3 == 2) and (board[2][2] == 1):
            pavlovs.append("Small Diagonal 2 in a row block reward")
            score += value
        elif (truth_3 == 1) and (board[2][2] == 2):
            pavlovs.append("Small Diagonal 2 in a row block punishment")
            score -= value
        if (truth_4 == 2) and (board[2][0] == 1):
            pavlovs.append("Small Diagonal 2 in a row block reward")
            score += value
        elif (truth_4 == 1) and (board[2][0] == 2):
            pavlovs.append("Small Diagonal 2 in a row block punishment")
            score -= value
        # Reward for getting two with a space between, punish for letting opponent get two with a space between
        if (
            board[0][0] == board[2][2] == 1
        ) and (board[1][1] == 0):
            pavlovs.append("Small Diagonal spaced 2 in a row reward")
            score += value
        elif (
            board[0][0] == board[2][2] == 2
        ) and (board[1][1] == 0):
            pavlovs.append("Small Diagonal spaced 2 in a row punishment")
            score -= value
        if (
            board[0][2] == board[2][0] == 1
        ) and (board[1][1] == 0):
            pavlovs.append("Small Diagonal spaced 2 in a row reward")
            score += value
        elif (
            board[0][2] == board[2][0] == 2
        ) and (board[1][1] == 0):
            score -= value
        # Reward for blocking two with a space between, punish for letting opponent block two with a space between
        if (
            board[0][0] == board[2][2] == 2
        ) and (board[1][1] == 1):
            pavlovs.append("Small Diagonal spaced 2 in a row block reward")
            score += value
        elif (
            board[0][0] == board[2][2] == 1
        ) and (board[1][1] == 2):
            pavlovs.append("Small Diagonal spaced 2 in a row block punishment")
            score -= value
        if (
            board[0][2] == board[2][0] == 2
        ) and (board[1][1] == 1):
            pavlovs.append("Small Diagonal spaced 2 in a row block reward")
            score += value
        elif (
            board[0][2] == board[2][0] == 1
        ) and (board[1][1] == 2):
            pavlovs.append("Small Diagonal spaced 2 in a row block punishment")
            score -= value
        return [score, pavlovs]