def solution(n):
    array = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        array[i][i] = 1
    return array
