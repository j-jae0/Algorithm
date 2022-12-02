def solution(polynomial):
    x = 0
    y = 0
    s_polynomial = polynomial.split(" + ")
    
    for p in s_polynomial:
        if p[-1] == 'x':
            if len(p) == 1:
                x += 1
            else:
                x += int(p[:-1])
        else:
            y += int(p)
            
    if x == 1 and y == 0:
        return "x"
    elif x==1 and y!= 0:
        return f"x + {y}"    
    elif x != 0 and y != 0:
        return f"{x}x + {y}" 
    elif x == 0 and y != 0:
        return f"{y}"
    elif y == 0 and x != 0:
        return f"{x}x"

