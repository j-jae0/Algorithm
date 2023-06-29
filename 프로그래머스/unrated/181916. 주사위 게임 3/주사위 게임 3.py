def solution(a, b, c, d):
    answer = 0
    dic = {k:0 for k in [a, b, c, d]}
    keys = list(dic.keys())
    # 딕셔너리에 키별로 value 입력
    for k in [a, b, c, d]:
        dic[k] += 1
    # 딕셔너리 value 값을 기준으로 오름차순 정렬
    reverse_dic = {v:k for k,v in dic.items()}    
    
    # 네 주사위 숫자가 모두 동일
    if len(keys) == 1:
        answer = 1111 * a
    # 주사위의 숫자가 3, 1 또는 2, 2 개씩 동일
    elif len(keys) == 2:
        if max(dic.values()) == 3:
            answer = (10 * reverse_dic[3] + reverse_dic[1])**2
        else:
            answer = (keys[0] + keys[1]) * abs(keys[0] - keys[1])
    # 주사위의 숫자가 2, 1, 1 인 경우    
    elif len(keys) == 3:
        condition_list = [k for k, v in dic.items() if v == 1]
        answer = condition_list[0] * condition_list[1]
    # 주사위의 숫자가 모두 다름
    else:
        answer = min([a, b, c, d])

    return answer