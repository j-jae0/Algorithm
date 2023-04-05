def solution(A, B):
    num = A
    # 동일한 경우
    if A == B:
        return 0

    for i in range(len(A)):
        num = num[-1] + num[:-1]
        if num == B:
            return i+1
    
    return -1