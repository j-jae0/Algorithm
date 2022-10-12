def solution(absolutes, signs):
    
    a = 0
    total = 0
    
    for i, num in enumerate(absolutes):
        if signs[i] == True:
            a = 1
        else:
            a = -1
            
        total += (num*a)
        
    return total