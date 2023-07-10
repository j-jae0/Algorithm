from itertools import combinations
def solution(numbers):
    comb = list(combinations(numbers, 2))
    add_comb = list(set([sum(c) for c in comb]))
    return sorted(add_comb)