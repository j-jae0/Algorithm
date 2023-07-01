def solution(my_string):
    dic = {k:0 for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}
    for s in my_string:
        dic[s] += 1
    return [v for v in dic.values()]