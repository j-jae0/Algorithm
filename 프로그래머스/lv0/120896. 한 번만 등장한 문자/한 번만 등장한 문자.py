def solution(s):
    num_dict = dict()
    answer = []
    # 문자별로 등장한 횟수가 담긴 사전 생성
    for alpha in s:
        if alpha in num_dict.keys():
            num_dict[alpha] += 1
        else:
            num_dict[alpha] = 1
            
    # 한 번만 등장한 문자 찾기
    for k, v in num_dict.items():
        if v == 1:
            answer.append(k)
    
    if len(answer) == 0:
        answer.append('')
    
    # 정렬
    answer.sort()
    return ''.join(answer)