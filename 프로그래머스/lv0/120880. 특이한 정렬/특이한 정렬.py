def solution(numlist, n):
    s_numlist = sorted(numlist, reverse=True)
    return sorted(s_numlist, key=lambda x:abs(n-x), reverse=False)