def minimax(node, depth, maximizingPlayer):
    if depth = 0 or node is terminal:
        return value 
    if maximizingPlayer:
        value = -infinity
        for child in children:
            value = max(value, minimax(child, depth-1, FALSE))
        return value
    else:
        value = infinity
        for child in children:
            value = min(value, minimax(child, depth-1, TRUE))
