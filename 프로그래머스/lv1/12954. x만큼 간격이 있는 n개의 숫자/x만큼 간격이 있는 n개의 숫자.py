def solution(x, n):
    answer = []
    # x가 0일 때
    if x == 0:
        answer = [0] * n
    # x가 음수일 때
    elif x < 0:
        for i in range(x, x*n-1, x):
            answer.append(i)
    # x가 양수일 때
    elif x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
        
    return answer