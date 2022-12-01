def solution(age):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    str_age = str(age)
    answer = ""
    
    for a in str_age:
        answer += alpha[int(a)]
        
    return answer 