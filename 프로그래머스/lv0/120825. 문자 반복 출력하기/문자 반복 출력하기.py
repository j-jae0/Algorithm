def solution(my_string, n):
    def fun(x):
        return x*n
    return "".join(list(map(fun, my_string)))