def solution(n, m, section):
    if len(section) == 1:
        return 1
    paints = [section[0]]
    for s in section[1:]:
        if paints[-1] + m > s:
            pass
        else:
            paints.append(s)
    return len(paints)