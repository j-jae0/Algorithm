def solution(arr, flag):
    l = []
    for i, f in zip(arr, flag):
        if f:
            for j in range(i):
                l.append(i)
                l.append(i)
        else:
            l = l[:-i]
    return l