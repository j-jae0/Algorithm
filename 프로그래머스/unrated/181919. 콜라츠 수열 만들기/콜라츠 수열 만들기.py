def solution(n):
    num = n
    num_list = [num]
    while num != 1:
        if num % 2 == 0: 
            num = num // 2
            num_list.append(num)
        else:
            num = num * 3 + 1
            num_list.append(num)
    return num_list