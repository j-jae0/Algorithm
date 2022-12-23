def solution(s):
    # 공백을 기준으로 나누기
    s = s.split(" ")
    answer = []
    for n in s:
        if n == 'Z':
            answer.append(answer[-1]*-1)
        else:
            answer.append(int(n))
    return sum(answer)