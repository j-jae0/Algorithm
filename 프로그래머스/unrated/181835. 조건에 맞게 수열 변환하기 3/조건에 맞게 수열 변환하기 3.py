def solution(arr, k):
    return [n+k for n in arr] if k % 2 == 0 else [m*k for m in arr]