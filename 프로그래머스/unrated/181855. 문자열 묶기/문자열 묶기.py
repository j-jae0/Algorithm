def solution(strArr):
    dic = {len(s):0 for s in strArr}
    for s in strArr:
        dic[len(s)] += 1
    return max(dic.values())