import random

from jenga import jenga_brute_force, jenga_smarter


def get_random_problem():
    n = random.randint(1, 10)
    columns = (random.randint(0, 10) for _ in range(n))
    C = random.randint(1, 10)
    E = random.randint(1, 10)
    M = random.randint(1, 10)
    return tuple(columns), C, E, M


for i in range(1000):
    n, C, E, M = get_random_problem()
    print(f"{i+1}: {C=} {E=} {M=} n={len(n)}")

    cost_brute, states_brute = jenga_brute_force(n, C, E, M)
    cost_smart, states = jenga_smarter(n, C, E, M)

    print(cost_smart, states[0])

    if cost_brute == cost_smart:
        print("Succed. Cost: ", cost_brute)
    else:
        print(f"Fail. {cost_brute=} {cost_smart=}")
