def solution(numbers):
    num_list = sorted(numbers, reverse=True)
    return num_list[0]*num_list[1]