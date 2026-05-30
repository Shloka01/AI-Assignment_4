def uct(node):

    if node.visits == 0:
        return float("inf")

    return (
        node.wins / node.visits
        +
        math.sqrt(
            2 * math.log(node.parent.visits)
            / node.visits
        )
    )
