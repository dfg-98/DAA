from random import random
from colorama import Fore
from generator import get_random_problem
from penga_binary_search import penga_binary
from penga_dinamic import penga_dinamic
from penga_exploration import penga_brute_force


def tester_dp(count_tests, max_value, max_C, max_E, max_M):
    for i in range(count_tests):
        n, C, E, M = get_random_problem(max_value, max_C, max_E, max_M)
        brute = penga_brute_force(n, C, E, M)
        dp_sol = penga_dinamic(n, C, E, M)
        print(Fore.WHITE, f"Test case: {C=} {E=} {M=} n={len(n)}")
        if brute[0] == dp_sol[0]:
            print(Fore.GREEN, dp_sol[0] ,"==" , brute[0] )
        else:
            print(Fore.RED, dp_sol[0],"==", brute[0])

def tester_binary(count_tests, max_value, max_C, max_E, max_M):
    for i in range(count_tests):
        n, C, E, M = get_random_problem(max_value, max_C, max_E, max_M)
        dp_sol = penga_dinamic(n, C, E, M)
        bi_sol = penga_binary(n, C, E, M)
        print(Fore.WHITE, f"Test case: {C=} {E=} {M=} n={len(n)}")
        if dp_sol[0] == bi_sol:
            print(Fore.GREEN, bi_sol ,"==" , dp_sol[0] )
        else:
            print(Fore.RED, bi_sol,"==", dp_sol[0])
            print(n)

N = 20
C = 100
E = 100
M = 100

#tester_dp(100, N, C, E, M)
tester_binary(100, N, C, E, M)