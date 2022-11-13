def solution(arr):
    answer = []
    a = 10
    
    for num in arr:
        
        if a != num:
            answer.append(num)
        else:
            pass
        
        a = num
    
    return answer