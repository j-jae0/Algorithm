def solution(common):
    # 등차수열
    diff = common[1] - common[0]
    if diff == common[2] - common[1]:
        return common[-1] + diff
    
    seq = common[1] / common[0]
    if seq == common[2] / common[1]:
        return common[-1] * seq