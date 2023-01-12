def solution(array):
    answer = []
    one = array[0]
    for n in array:
        if n > one:
            one = n
    return [one, array.index(one)]