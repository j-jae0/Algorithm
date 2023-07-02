def solution(num_list):
    num = 1
    if len(num_list) > 10:
        return sum(num_list)
    else:
        for n in num_list: 
            num *= n
    return num