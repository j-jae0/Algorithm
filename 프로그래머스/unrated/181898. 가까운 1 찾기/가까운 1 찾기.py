def solution(arr, idx):
    new_arr = arr[idx:]
    if 1 not in new_arr:
        return -1
    else:
        return new_arr.index(1) + idx