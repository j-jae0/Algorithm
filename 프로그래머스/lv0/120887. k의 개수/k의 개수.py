def solution(i, j, k):
    answer = [str(n) for n in range(i, j+1)]
    return ''.join(answer).count(str(k))