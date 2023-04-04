def solution(num, total):
    num_list = list(range(-1000, num*1000))

    for i in range(0, len(num_list)):
        if sum(num_list[i:i+num]) == total:
            return num_list[i:i+num]