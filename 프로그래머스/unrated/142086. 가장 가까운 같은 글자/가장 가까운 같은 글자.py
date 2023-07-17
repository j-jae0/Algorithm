def solution(s):
    dic = {'0':0}
    answer = []
    for alpha in s:
        if alpha not in dic.keys():
            answer.append(-1)
            dic[alpha] = 0
            for dk in dic.keys():
                dic[dk] += 1
        else:
            answer.append(dic[alpha])
            dic[alpha] = 0
            for dk in dic.keys():
                dic[dk] += 1
    return answer