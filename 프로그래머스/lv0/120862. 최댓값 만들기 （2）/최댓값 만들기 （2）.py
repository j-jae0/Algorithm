# combination 함수로 리스트 내의 여러 항들을 특정 개수로 묶을 수 있다.(조합 가능)
from itertools import *

def solution(numbers):
    return max([c[0] * c[1] for c in list(combinations(numbers, 2))])