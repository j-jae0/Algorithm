from itertools import combinations

def solution(nums): 
    comb = list(combinations(nums, 3))
    sum_comb = sorted([sum(c) for c in comb])
    prime = set(range(7, max(sum_comb)+1))
    for p in list(prime):
        for q in range(2, p):
            if p % q == 0:
                prime -= set(range(2*q, p+1, q))
    return len([num for num in sum_comb if num in list(prime)])