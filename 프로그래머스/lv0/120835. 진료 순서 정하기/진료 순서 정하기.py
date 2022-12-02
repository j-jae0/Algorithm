def solution(emergency):
    answer = []
    
    ordered_e = sorted(emergency, reverse=True)
    answer = [ordered_e.index(n)+1 for n in emergency]
    
    # for n in emergency:
    #     answer.append(ordered_e.index(n) + 1) 
    
    return answer