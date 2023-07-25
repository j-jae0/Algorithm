def solution(k, m, score):
    score = sorted([s for s in score if s <= k])[::-1]
    apple_box, box = list(), list()
    for s in score:
        box.append(s)
        if len(box) // m == 1:
            apple_box.append(box)
            box = []
    return sum([min(apples) for apples in apple_box]) * m
            