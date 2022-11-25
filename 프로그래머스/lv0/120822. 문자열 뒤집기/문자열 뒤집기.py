def solution(my_string):

    return "".join([my_string[i] for i in range(-1, (len(my_string)+1)*-1, -1)])