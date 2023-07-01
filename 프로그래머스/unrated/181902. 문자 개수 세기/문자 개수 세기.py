def solution(my_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    dic = {k:0 for k in alpha}
    for s in my_string:
        dic[s] += 1
    return [v for v in dic.values()]