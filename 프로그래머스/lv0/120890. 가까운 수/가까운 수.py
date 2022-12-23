def solution(array, n):
    sorted_array = sorted(array, reverse=False)
    answer = sorted(sorted_array, reverse=False, key=lambda x: abs(x-n))
    return answer[0]