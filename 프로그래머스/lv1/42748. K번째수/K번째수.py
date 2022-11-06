def solution(array, commands):
    answer = []
    
    i = None
    j = None
    a = None
    
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        
        a = sorted(array[i-1:j])
        answer.append(a[k-1])
        
    return answer