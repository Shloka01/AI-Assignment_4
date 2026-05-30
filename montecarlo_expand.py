def expand(node):

    for move in node.state.legal_moves():

        child_state = node.state.make_move(move)

        child = MCTSNode(
            child_state,
            parent=node
        )

        node.children.append(child)

    return random.choice(node.children)
