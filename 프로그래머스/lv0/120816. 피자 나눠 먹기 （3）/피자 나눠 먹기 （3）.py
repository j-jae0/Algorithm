def solution(slice, n):
    # 피자의 조각 수는 최소 2
    for i in range(1, n*2+1):
        if (slice*i)//n >= 1:
            return i
            break
