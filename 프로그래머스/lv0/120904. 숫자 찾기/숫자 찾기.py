def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    if str_k not in str_num:
        return -1
    else: 
        return str_num.index(str_k) + 1