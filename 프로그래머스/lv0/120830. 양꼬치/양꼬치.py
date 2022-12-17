def solution(n, k):
    # service = n // 10
    # k_num = k - service    
    # return 12000*n + 2000*k_num
    
    return 12000*n + 2000*(k - n//10)