def solution(arr):
    for i, a in enumerate(arr):
        for j in range(len(a)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1