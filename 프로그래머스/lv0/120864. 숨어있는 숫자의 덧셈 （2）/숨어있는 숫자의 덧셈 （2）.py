def solution(my_string):
    answer = ''
    
    for s in my_string:
        if s.isalpha():
            answer += ' '
        else:
            answer += s
            
    return sum([int(n) for n in answer.split()])