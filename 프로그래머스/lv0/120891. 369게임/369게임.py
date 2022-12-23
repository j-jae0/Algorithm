def solution(order):
    return len([int(n) for n in str(order) if n in '369'])