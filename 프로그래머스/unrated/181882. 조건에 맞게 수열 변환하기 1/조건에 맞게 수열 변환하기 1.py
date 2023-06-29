def solution(arr):
    l = []
    for a in arr:
        if a >= 50 and a % 2 == 0:
            l.append(a//2)
        elif a < 50 and a % 2 != 0:
            l.append(a*2)
        else:
            l.append(a)
    return l