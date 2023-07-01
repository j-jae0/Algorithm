def solution(arr, k):
    l = []
    for a in arr:
        if a not in l:
            l.append(a)
    
    # 배열의 길이가 k보다 작은 경우 -1로 채우는 과정
    while len(l) < k:
        l.append(-1)
        
    return l[:k]