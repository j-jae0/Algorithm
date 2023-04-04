def solution(dots):
    x1, y1 = dots[0][0], dots[0][1]

    for dot in dots[1:]:
        if x1 != dot[0] and y1 == dot[1]:
            x2 = dot[0]
        elif x1 == dot[0] and y1 != dot[1]:
            y2 = dot[1]
    
    return abs(x1-x2) * abs(y1-y2)