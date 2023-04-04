import sys


def penga_dinamic(h, C, E, M):
    """
    O(n|h_max-h_min|)
    """
    h_max = max(h)
    h_min = min(h)

    COSTS = [[(0, 0) for _ in range(h_max + 1)] for _ in range(len(h) + 1)]

    for i in range(1, len(h) + 1):
        for j in range(h_min, h_max + 1):
            if j > h[i - 1]:
                c = j - h[i - 1]
                t = COSTS[i - 1][j]
                COSTS[i][j] = (t[0] + c, t[1])
            else:
                e = h[i - 1] - j
                t = COSTS[i - 1][j]
                COSTS[i][j] = (t[0], t[1] + e)

    min_cost = sys.maxsize
    for cost in COSTS[len(h)][h_min:]:
        if cost[0] < cost[1]:
            c = cost[0] * C + cost[1] * E
            min_cost = min(min_cost, c)
            c = (cost[1] - cost[0]) * E + cost[0] * M
            min_cost = min(min_cost, c)
            c = cost[1] * M + (cost[1] - cost[0]) * C
            min_cost = min(min_cost, c)
        else:
            e = cost[0] * C + cost[1] * E
            min_cost = min(min_cost, e)
            e = (cost[0] - cost[1]) * C + cost[1] * M
            min_cost = min(min_cost, e)
            e = cost[0] * M + (cost[0] - cost[1]) * E
            min_cost = min(min_cost, e)

    return min_cost, COSTS