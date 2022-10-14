def solution(array, n):
    
    answer = []
    for num in array:
        if num == n:
            answer.append(n)
        
    return len(answer)