def solution(players, callings):
    dic = {name:idx for idx, name in enumerate(players)}
    reverse_dic = {idx:name for idx, name in enumerate(players)}
    for c in callings: 
        dic[c] -= 1
        dic[reverse_dic[dic[c]]] += 1
        reverse_dic[dic[c]+1] = reverse_dic[dic[c]]
        reverse_dic[dic[c]] = c
    result = list(reverse_dic.values())
    return result