def solution(sides):
    
    s = sorted(sides, reverse=True)
    l = s[0]
    o = sum(s[1:])
    
    if l >= o:
        return 2
    else:
        return 1
