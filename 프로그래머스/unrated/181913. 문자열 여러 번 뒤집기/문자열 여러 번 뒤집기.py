def solution(my_string, queries):
    answer = list(my_string)
    for q in queries:
        answer[q[0]:q[1]+1] = answer[q[0]:q[1]+1][::-1]
    return ''.join(answer)