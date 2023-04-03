import random

from jenga import jenga_brute_force, jenga_smarter, penga


def get_random_problem():
    n = random.randint(1, 10**4)
    columns = (random.randint(0, 10**4) for _ in range(n))
    C = random.randint(1, 100)
    E = random.randint(1, 100)
    M = random.randint(1, 100)
    return tuple(columns), C, E, M


for i in range(10):
    n, C, E, M = get_random_problem()
    print(f"{i+1}: {C=} {E=} {M=} n={len(n)}")
   # print(n)
    # cost_brute, states_brute = jenga_brute_force(n, C, E, M)
    #cost, COSTS = penga(n, C, E, M)

    # if cost_brute == cost_smart:
    #     print("Succed. Cost: ", cost_brute)
    # else:
    #     print(f"Fail. {cost_brute=} {cost_smart=}")
