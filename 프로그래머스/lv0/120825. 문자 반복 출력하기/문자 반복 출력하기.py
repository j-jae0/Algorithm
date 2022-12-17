def solution(my_string, n):
    # def fun(x):
    #     return x*n
    # return "".join(list(map(fun, my_string)))
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[i]*n
    return answer