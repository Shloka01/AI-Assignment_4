import math

def minimax(node, depth, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        best = -math.inf

        for child in node.get_children():
            value = minimax(child, depth - 1, False)
            best = max(best, value)

        return best

    else:
        best = math.inf

        for child in node.get_children():
            value = minimax(child, depth - 1, True)
            best = min(best, value)

        return best
