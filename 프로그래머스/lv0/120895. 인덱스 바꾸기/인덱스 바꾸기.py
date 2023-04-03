def solution(my_string, num1, num2):
    # 저장할 최종 문자열 
    answer = ''
    
    # 변경
    for i, s in enumerate(my_string):
        if i != num1 and i != num2:
            answer += s
        elif i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
    return answer