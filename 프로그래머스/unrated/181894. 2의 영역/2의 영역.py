def solution(arr):
    # 2가 존재하지 않는 경우
    if 2 not in arr:
        return [-1]
    
    # 배열의 첫 번째 요소와 마지막 요소가 2인 경우(배열 그대로를 출력)
    if arr[0] == 2 and arr[-1] == 2:
        return arr

    # 그 외의 케이스
    idx = arr.index(2)
    reverse_idx = -arr[::-1].index(2)
    return arr[idx:reverse_idx]