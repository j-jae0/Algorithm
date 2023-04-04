def solution(my_string):
    # 공백 제거
    my_string = my_string.split()
    # 첫 번째 숫자 저장해 두기
    answer = int(my_string[0])
    
    # 연산 과정
    for i, n in enumerate(my_string):
        if n == '+':
            answer += int(my_string[i+1])
        elif n == '-':
            answer -= int(my_string[i+1])
    
    return int(answer)
    