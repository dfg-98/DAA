import random


def get_random_problem(m_len, m_c, m_e, m_m):
    n = random.randint(1, m_len)
    columns = (random.randint(0, m_len) for _ in range(n))
    C = random.randint(1, m_c)
    E = random.randint(1, m_e)
    M = random.randint(1, m_m)
    n = tuple(columns)
    return n, C, E, M
