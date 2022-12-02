def solution(numlist, n):
    s_numlist = sorted(numlist, reverse=True)
    answer = sorted(s_numlist, key=lambda x:abs(n-x), reverse=False)
    return answer