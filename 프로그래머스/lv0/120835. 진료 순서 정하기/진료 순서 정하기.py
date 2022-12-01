def solution(emergency):
    answer = []
    
    ordered_e = sorted(emergency, reverse=True)
    for n in emergency:
        answer.append(ordered_e.index(n) + 1) 
    
    return answer