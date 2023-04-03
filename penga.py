def penga(h, C, E, M):
    """
    O(n log(|h_max-h_min|))
    """
    low = 0
    top = max(h)

    while top - low > 1:
        mid = (top + low) // 2
        mid_cost = penga_goal(h, C, E, M, mid)
        next_cost = penga_goal(h, C, E, M, mid + 1)
        if mid_cost >= next_cost:
            low = mid
        else:
            top = mid

    return penga_goal(h, C, E, M, top)


def penga_goal(h, C, E, M, goal):
    """
    O(n)
    """
    n = len(h)
    moves = [0, 0]

    for i in range(n):
        if h[i - 1] < goal:
            c = goal - h[i - 1]
            moves[0] += c
        else:
            e = h[i - 1] - goal
            moves[1] += e

    min_cost = moves[0] * C + moves[1] * E
    if moves[0] < moves[1]:
        c = (moves[1] - moves[0]) * E + moves[0] * M
        min_cost = min(min_cost, c)
        c = moves[1] * M + (moves[1] - moves[0]) * C
        min_cost = min(min_cost, c)
    else:
        e = (moves[0] - moves[1]) * C + moves[1] * M
        min_cost = min(min_cost, e)
        e = moves[0] * M + (moves[0] - moves[1]) * E
        min_cost = min(min_cost, e)

    return min_cost


h = [3, 2, 1]
C = 1
E = 10
M = 8
c = penga(h, C, E, M)
print(c)
