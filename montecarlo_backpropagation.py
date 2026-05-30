def backpropagate(node, result):

    while node:

        node.visits += 1
        node.wins += result

        node = node.parent
