def solution(k, m, score):
    score = sorted([s for s in score if s <= k])[::-1]
    apple_box, box = list(), list()
    
    if len(score) // m == 1:
        apple_box = score[:m]
        return min(apple_box) * m
    
    for s in score:
        box.append(s)
        if len(box) // m == 1:
            apple_box.append(box)
            box = []
    return sum([len(apples) * min(apples) for apples in apple_box])
            