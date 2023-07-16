def solution(s):
    x, y = 0, 0
    first_alpha = False
    answer = 0
    
    for idx, alpha in enumerate(s):
        if not first_alpha:
            first_alpha = alpha
            x += 1
        elif alpha == first_alpha:
            x += 1
        else:
            y += 1
        
        if x == y:
            x, y = 0, 0
            first_alpha = False
            answer += 1
    if x != 0 or y != 0:
        answer += 1
    return answer