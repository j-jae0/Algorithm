def solution(arr, flag):
    l = []
    for a, f in zip(arr, flag):
        if f:
            for _ in range(a):
                l.extend([a, a])
        else:
            l = l[:-a]
    return l