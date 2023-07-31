def solution(k, score):
    answer = []
    for i in range(len(score)):
        score_list = sorted(score[:i+1])[::-1]
        if len(score_list) < k:
            answer.append(score_list[-1])
        else:
            answer.append(score_list[k-1])
    return answer