def solution(dots):
    dot = dots[0]
    dots = dots[1:]
    for i in range(len(dots)):
        dx1 = dot[0] - dots[i][0]
        dy1 = dot[1] - dots[i][1]
        
        dx2 = dots[i-1][0] - dots[i-2][0]
        dy2 = dots[i-1][1] - dots[i-2][1]
        
        slope1 = dy1/dx1
        slope2 = dy2/dx2
        
        if slope1 == slope2:
            return 1
        
    return 0