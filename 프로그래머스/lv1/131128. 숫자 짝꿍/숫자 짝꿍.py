def solution(X, Y):
    if len(set(X) & set(Y)) == 0:
        return "-1"
    answer = ""
    for n in range(10):
        answer += str(n) * min([X.count(str(n)), Y.count(str(n))])
    return answer[::-1] if len(set(answer)) > 1 else answer[0]