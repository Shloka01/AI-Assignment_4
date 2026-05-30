def mcts(root, iterations=1000):

    for _ in range(iterations):

        node = select(root)

        if not node.state.is_terminal():
            node = expand(node)

        result = simulate(node.state)

        backpropagate(node, result)

    return max(
        root.children,
        key=lambda c: c.visits
    )
