import heapq

def astar(start,
          goal,
          graph,
          heuristic):

    pq = []

    heapq.heappush(
        pq,
        (0, start)
    )

    cost = {
        start: 0
    }

    parent = {
        start: None
    }

    while pq:

        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor in graph[current]:

            new_cost = (
                cost[current]
                +
                graph[current][neighbor]
            )

            if (neighbor not in cost
                    or
                    new_cost < cost[neighbor]):

                cost[neighbor] = new_cost

                priority = (
                    new_cost
                    +
                    heuristic[neighbor]
                )

                heapq.heappush(
                    pq,
                    (priority, neighbor)
                )

                parent[neighbor] = current

    path = []

    node = goal

    while node:

        path.append(node)
        node = parent[node]

    path.reverse()

    return path
