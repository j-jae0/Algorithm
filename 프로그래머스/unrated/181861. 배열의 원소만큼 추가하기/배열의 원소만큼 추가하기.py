def solution(arr):
    l = []
    for n in arr:
        for _ in range(n):
            l.append(n)
    return l