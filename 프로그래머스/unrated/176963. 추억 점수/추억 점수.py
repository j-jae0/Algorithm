def solution(name, yearning, photo):
    dic = {n:y for n, y in zip(name, yearning)}
    l = []
    for p in photo:
        point = 0
        for n in p:
            if n in name:
                point += dic[n]
        l.append(point)
    return l