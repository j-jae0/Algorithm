def solution(arr, n):
    odd = [j+n if i%2==0 else j for i, j in enumerate(arr)]
    even = [j+n if i%2!=0 else j for i, j in enumerate(arr)]
    return even if len(arr) % 2 == 0 else odd