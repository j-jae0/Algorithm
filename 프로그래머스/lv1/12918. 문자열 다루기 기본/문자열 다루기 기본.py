def solution(s):

    list_s = list(s)
    f = []

    try:
        for i in list_s:
            int(s)
            f.append(s)
            
    except:
        pass
    
    return (len(f) == 4) or (len(f) == 6)
        
        