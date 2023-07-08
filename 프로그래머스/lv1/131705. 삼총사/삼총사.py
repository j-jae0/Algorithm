from itertools import combinations

def solution(number):
    comb = list(combinations(number, 3))
    return len([c for c in comb if sum(c) == 0])