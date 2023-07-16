def solution(s):
    l = []
    x, y = 0, 0
    first_alpha = False
    new_string = ''
    
    for idx, alpha in enumerate(s):
        if not first_alpha:
            first_alpha = alpha
            new_string += alpha
            x += 1
        elif alpha == first_alpha:
            new_string += alpha
            x += 1
        else:
            new_string += alpha
            y += 1
        
        if x == y:
            l.append(new_string)
            x, y = 0, 0
            first_alpha = False
            new_string = ''
    
    if len(new_string) > 0:
        l.append(new_string)
    return len(l)