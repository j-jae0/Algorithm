def solution(n):
    arr = [[0 for i in range(n)] for j in range(n)]
    for k in range(n):
        arr[k][k] = 1
    return arr