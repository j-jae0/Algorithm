def solution(arr):
    if 2 not in arr:
        return [-1]
    if arr[0] == 2 and arr[-1] == 2:
        return arr
    idx = arr.index(2)
    reverse_idx = arr[::-1].index(2)*-1 -1
    return arr[idx:reverse_idx+1]