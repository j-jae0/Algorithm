def solution(num_list, n):
    lr = num_list[n:] + num_list[:n-1]
    lr.append(num_list[n-1])
    return lr