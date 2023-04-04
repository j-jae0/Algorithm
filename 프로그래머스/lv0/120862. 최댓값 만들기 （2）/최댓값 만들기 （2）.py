from itertools import *

def solution(numbers):
    return max([c[0] * c[1] for c in list(combinations(numbers, 2))])