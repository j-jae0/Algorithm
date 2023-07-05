def solution(arr):
    if len(arr) == 1:
        return arr
    
    l = min([2**i for i in range(1, len(arr)//2+1) if 2**i >= len(arr)])
    for _ in range(l-len(arr)):
        arr.append(0)
    return arr