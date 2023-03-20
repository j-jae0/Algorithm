def solution(n):
    answer = 2
    for m in range(1, n):
        if n == m*m:
            answer = 1
            break
    return answer