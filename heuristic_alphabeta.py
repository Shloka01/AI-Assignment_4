import math

def heuristic_alpha_beta(node,
                         depth,
                         alpha,
                         beta,
                         maximizing_player):

    if depth == 0 or node.is_terminal():
        return node.heuristic()

    if maximizing_player:

        value = -math.inf

        for child in node.get_children():

            value = max(
                value,
                heuristic_alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    False
                )
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for child in node.get_children():

            value = min(
                value,
                heuristic_alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    True
                )
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value
