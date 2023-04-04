def solution(my_string):
    answer = [s for s in my_string.lower()]
    answer.sort()
    return ''.join(answer)