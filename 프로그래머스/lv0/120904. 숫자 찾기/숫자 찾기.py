def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    return -1 if str_k not in str_num else str_num.index(str_k) + 1