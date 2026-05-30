def select(node):

    while node.children:
        node = max(node.children, key=uct)

    return node
