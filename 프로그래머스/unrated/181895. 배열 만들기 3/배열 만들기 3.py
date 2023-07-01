def solution(arr, intervals):
    l = []
    for i in intervals:
        l.extend(arr[i[0]:i[1]+1])
    return l