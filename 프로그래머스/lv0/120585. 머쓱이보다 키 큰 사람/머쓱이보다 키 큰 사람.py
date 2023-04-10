def solution(array, height):
    answer = []
    for h in array:
        if h > height:
            answer.append(0)    
    return len(answer)