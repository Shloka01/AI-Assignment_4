def simulate(state):

    current = state.copy()

    while not current.is_terminal():

        move = random.choice(
            current.legal_moves()
        )

        current = current.make_move(move)

    return current.result()
