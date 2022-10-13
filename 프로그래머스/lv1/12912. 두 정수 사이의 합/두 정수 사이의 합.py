def solution(a, b):
    s_num = 0
    l_num = 0
    
    if a >= b:
        s_num = b
        l_num = a
    elif a < b:
        s_num = a
        l_num = b
    
    total = []
    for i in range(s_num, l_num+1):
        total.append(i)
        
    return sum(total)