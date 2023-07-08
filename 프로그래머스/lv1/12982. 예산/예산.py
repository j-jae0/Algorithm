from itertools import combinations

def solution(d, budget):
    sorted_d = sorted(d)
    if sum(sorted_d) <= budget:
        return len(sorted_d)
    for i in range(len(sorted_d)):
        if sum(sorted_d[:-1-i]) <= budget:
            return len(sorted_d) - i - 1
    
    # group_num = len(d) - 1
    # for i in range(group_num):
    #     group_list = list(combinations(d, group_num))
    #     sum_group_list = [sum(g) for g in group_list]
    #     if min(sum_group_list) <= budget:
    #         break
    #     else:
    #         group_num -= 1
    return group_num