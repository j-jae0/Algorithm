def solution(strings, n):
    strings = sorted(strings)
    s = sorted(strings, key=lambda x : x[n])
    return s